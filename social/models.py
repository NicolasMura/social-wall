# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # utile ?

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.encoding import python_2_unicode_compatible  # utile ?
# from django.core.exceptions import ValidationError

COMMENT_MAX_LENGTH = 1000
VALID_IMG_EXTENSIONS = [
        ".jpg",
        ".jpeg",
        '.png',
        ".gif",
    ]
MEGABYTE_LIMIT = 2
MAX_WIDTH = 1920
MAX_HEIGHT = 1080


# def validate_image(
#         fieldfile_obj,
#         max_width=MAX_WIDTH,
#         max_height=MAX_HEIGHT,
#         max_size=MEGABYTE_LIMIT*1024*1024,
#         valid_extensions=VALID_IMG_EXTENSIONS):
#     if fieldfile_obj.file is None or fieldfile_obj.file.image is None:
#         raise ValidationError("Erreur : fichier absent.")
#     if not fieldfile_obj.file.name.endswith(tuple(VALID_IMG_EXTENSIONS)):
#         raise ValidationError(
#             "Erreur : le format de l'image est incorrect ! "
#             "(Formats autorisés : {})".format(VALID_IMG_EXTENSIONS))
#     if (
#         fieldfile_obj.file.image.width > max_width or
#         fieldfile_obj.file.image.height > max_height
#     ):
#         raise ValidationError(
#             "Erreur : l'image n'est pas au format autorisé (600 x 174 px).")
#     if fieldfile_obj.file.image.size > max_size:
#         raise ValidationError(
#             "L'image dépasse la taille maximale "
#             "autorisée ({} Mo)".format(MEGABYTE_LIMIT))


class Profile(AbstractUser):
    class Meta:
        verbose_name = 'Profil utilisateur'
        verbose_name_plural = 'Profils utilisateurs'

    avatar = models.FileField(
        verbose_name="Votre avatar",
        blank=True,
        null=False,
        upload_to='upload/avatars',
        default='upload/avatars/default-avatar.png',
        # validators=[validate_image],
    )

    def __str__(self):
        return self.username


# @python_2_unicode_compatible
class PostCommentAbstract(models.Model):
    """
    A user post/comment about some object.
    """

    class Meta:
        abstract = True
        ordering = ('submit_date', )

    # profile = models.ForeignKey(
    #     # settings.AUTH_USER_MODEL,
    #     'social.Profile',
    #     verbose_name='profile',
    #     blank=True,
    #     null=True,
    #     related_name="%(class)s_comments",
    #     on_delete=models.SET_NULL,
    # )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Auteur',
        blank=False,
        null=False,
        # related_name="%(class)s_comments",
        related_name="%(class)s_author",
        # on_delete=models.SET_NULL,
    )
    content = models.CharField(
        verbose_name='Commentaire',
        max_length=COMMENT_MAX_LENGTH,
        default="",
        blank=False,
    )

    # Metadata about the comment
    submit_date = models.DateTimeField(
        verbose_name='Date de publication',
        auto_now_add=True,
        auto_now=False,
    )
    is_public = models.BooleanField(
        verbose_name='public ?',
        default=True,
        help_text='Uncheck this box to make the comment effectively '
        'disappear from the site.',
    )
    is_removed = models.BooleanField(
        verbose_name='Désactivé ?',
        default=False,
        help_text='Check this box if the comment is inappropriate. '
        'A "This comment has been removed" message will '
        'be displayed instead.',
    )

    def __str__(self):
        return "%s: %s..." % (self.author, self.content[:50])

    # def __str__(self):
    #     return "Commentaire {0}".format(self.content)

    def get_absolute_url(self, anchor_pattern="#c%(id)s"):
        return self.get_content_object_url() + (anchor_pattern % self.__dict__)

    def get_as_text(self):
        """
        Return this comment as plain text.  Useful for emails.
        """
        d = {
            'profile': self.profile,
            'date': self.submit_date,
            'comment': self.comment,
            'domain': self.site.domain,
        }
        return 'Posted by %(author)s '
        'at %(date)s\n\n%(comment)s\n\nhttp://%(domain)s%(url)s' % d


class Post(PostCommentAbstract):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    comments = models.ManyToManyField(
        'social.Comment',
        blank=True,
        null=True,
        verbose_name='Commentaires relatifs',
        related_name='comments',
    )
    wall = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Publié sur le mur de',
        blank=False,
        null=False,
        # related_name="%(class)s_comments",
        related_name="wall",
    )


class Comment(PostCommentAbstract):
    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    post = models.ForeignKey(
        'social.Post',
        verbose_name='Post relatif',
        blank=False,
        null=False,
        related_name="%(class)s_comments",
        # on_delete=models.SET_NULL,
        )
