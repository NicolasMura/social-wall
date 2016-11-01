# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # utile ?

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.encoding import python_2_unicode_compatible  # utile ?

COMMENT_MAX_LENGTH = 3000


class Profile(AbstractUser):
    class Meta:
        verbose_name = 'Profil utilisateur'
        verbose_name_plural = 'Profils utilisateurs'

    avatar = models.FileField(
        verbose_name="Votre avatar",
        # null=True,
        blank=True,
        upload_to='upload/avatars',
        default='upload/avatars/default-avatar.png'
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
        verbose_name = 'comment'
        verbose_name_plural = 'comments',

    # profile = models.ForeignKey(
    #     # settings.AUTH_USER_MODEL,
    #     'social.Profile',
    #     verbose_name='profile',
    #     blank=True,
    #     null=True,
    #     related_name="%(class)s_comments",
    #     on_delete=models.SET_NULL,
    # )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Profil',
        blank=True,
        null=True,
        # related_name="%(class)s_comments",
        related_name="%(class)s_comments",
        on_delete=models.SET_NULL,
    )
    content = models.CharField(
        verbose_name='Commentaire',
        max_length=COMMENT_MAX_LENGTH,
        null=False,
        blank=False,
    )

    # Metadata about the comment
    submit_date = models.DateTimeField(
        verbose_name='date/time submitted',
        auto_now_add=True,
        auto_now=False,
    )
    is_public = models.BooleanField(
        verbose_name='is public',
        default=True,
        help_text='Uncheck this box to make the comment effectively '
        'disappear from the site.',
    )
    is_removed = models.BooleanField(
        verbose_name='is removed',
        default=False,
        help_text='Check this box if the comment is inappropriate. '
        'A "This comment has been removed" message will '
        'be displayed instead.',
    )

    def __str__(self):
        return "%s: %s..." % (self.user, self.content[:50])

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
        return 'Posted by %(user)s '
        'at %(date)s\n\n%(comment)s\n\nhttp://%(domain)s%(url)s' % d


class Post(PostCommentAbstract):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    comments = models.ManyToManyField(
        'social.Comment',
        verbose_name='Commentaires relatifs',
        related_name='comments',
    )


class Comment(PostCommentAbstract):
    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    # post = models.ForeignKey(
    #     'social.Post',
    #     verbose_name='Post relatif',
    #     blank=True,
    #     null=True,
    #     related_name="%(class)s_comments",
    #     on_delete=models.SET_NULL,
    #     )
