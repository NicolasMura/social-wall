# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
# from django.contrib.sites.models import Site  # utile ?
# from django.utils.encoding import python_2_unicode_compatible  # utile ?


VALID_IMG_EXTENSIONS = [
        ".jpg", ".JPG",
        ".jpeg", ".JPEG",
        ".png", ".PNG",
        ".gif", ".GIF",
    ]
MEGABYTE_LIMIT = 2
MAX_WIDTH = 6000
MAX_HEIGHT = 6000


def validate_image(
        fieldfile_obj,
        max_width=MAX_WIDTH,
        max_height=MAX_HEIGHT,
        max_size=MEGABYTE_LIMIT*1024*1024,
        valid_extensions=VALID_IMG_EXTENSIONS):
    # Below condition is for robustness only
    if not fieldfile_obj.file.name.endswith(tuple(VALID_IMG_EXTENSIONS)):
            raise ValidationError(_(
                "Erreur : le format de l'image est incorrect ! "
                "(Formats autorisés : {})".format(VALID_IMG_EXTENSIONS)))
    if hasattr(fieldfile_obj.file, 'image'):
        if (
            fieldfile_obj.file.image.width > max_width or
            fieldfile_obj.file.image.height > max_height
        ):
            raise ValidationError(_(
                "Erreur : les dimensions de l'image excèdent le maximum "
                "autorisé ({} x {} max).").format(MAX_WIDTH, MAX_HEIGHT))
        img_width = fieldfile_obj.file.image.size[0]
        img_height = fieldfile_obj.file.image.size[1]
        if img_width*img_height > max_size:
            raise ValidationError(_(
                "L'image dépasse la taille maximale "
                "autorisée ({} Mo)".format(MEGABYTE_LIMIT)))


class Profile(AbstractUser):
    class Meta:
        verbose_name = _('Utilisateur')
        verbose_name_plural = _('Utilisateurs')

    avatar = models.ImageField(
        verbose_name=_("Votre avatar"),
        blank=True,
        null=False,
        upload_to='upload/avatars',
        default='default/avatars/default-avatar.png',
        validators=[validate_image],
    )

    def __unicode__(self):
        return self.username
