# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0010_auto_20161027_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(upload_to='upload/avatars', verbose_name='Votre avatar', blank=True, default='upload/avatars/default-avatar.png'),
        ),
    ]
