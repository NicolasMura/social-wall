# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.sites.models import Site  # utile ?
from django.utils import timezone
# from django.utils.encoding import python_2_unicode_compatible  # utile ?
# from django.core.exceptions import ValidationError


def get_elapsed_time(date_start, date_end):
    MONTHS = {
        1: 'janvier',
        2: 'février',
        3: 'mars',
        4: 'avril',
        5: 'mai',
        6: 'juin',
        7: 'juillet',
        8: 'août',
        9: 'septembre',
        10: 'octobre',
        11: 'novembre',
        12: 'décembre',
    }

    if date_start > date_end:
        raise ValueError('date_end must be greater that date_start')
    day_number_start = date_start.month*12 + date_start.day
    day_number_end = date_end.month*12 + date_end.day
    # If start day and end day are the same
    if day_number_start == day_number_end:
        past_seconds_from_date = (date_end - date_start).seconds
        if past_seconds_from_date < 60:
            past_time_from_date = 'Il y a moins d\'une minute'
        elif past_seconds_from_date < 3600:
            past_minutes_from_date = past_seconds_from_date / 60
            if past_minutes_from_date < 2:
                past_time_from_date = 'Il y a 1 minute'
            else:
                past_time_from_date = 'Il y a {} minutes'.format(
                    int(round(past_minutes_from_date, 0)))
        elif past_seconds_from_date < 86400:
            past_hours_from_date = past_seconds_from_date / 3600
            if past_hours_from_date < 2:
                past_time_from_date = 'Il y a 1 heure'
            else:
                past_time_from_date = 'Il y a {} heures'.format(
                    int(round(past_hours_from_date, 0)))
        else:
            past_time_from_date = date_start
    # If start day is the day before end day
    elif day_number_start == (day_number_end-1):
        past_time_from_date = 'Hier, à {}'.format(
            date_start.time().strftime('%Hh%M'))
    # Else, start day is more or equal than 2 days before end day
    else:
        past_time_from_date = 'Le {} {}, à {}'.format(
            date_start.strftime('%d'),
            MONTHS[date_start.month],
            date_start.time().strftime('%Hh%M'))

    # Reste le cas particulier du 1er janvier à traiter !

    return past_time_from_date

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
        default='static/avatars/default-avatar.png',
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

    def get_past_time_from_submit_date(self):
        now = timezone.now()
        past_time_from_submit_date = get_elapsed_time(self.submit_date, now)

        return past_time_from_submit_date

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
        return 'Posted by %(profile)s '
        'at %(date)s\n\n%(comment)s\n\nhttp://%(domain)s' % d


class Post(PostCommentAbstract):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    wall = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Publié sur le mur de',
        blank=False,
        null=False,
        # related_name="%(class)s_comments",
        related_name="wall",
    )

    def __str__(self):
        return "Post de %s : %s..." % (self.author, self.content[:50])


class Comment(PostCommentAbstract):
    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    related_post = models.ForeignKey(
        'social.Post',
        verbose_name='Post relatif',
        blank=False,
        null=False,
        # related_name="%(class)s_comments",
        # on_delete=models.SET_NULL,
        # related_name="wall",
        )

    def __str__(self):
        return "Commentaire de %s : %s..." % (self.author, self.content[:50])
