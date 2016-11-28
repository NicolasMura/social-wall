# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import social.models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0018_auto_20161128_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(verbose_name='Votre avatar', validators=[social.models.validate_image], default='default/avatars/default-avatar.png', upload_to='upload/avatars', blank=True),
        ),
    ]
