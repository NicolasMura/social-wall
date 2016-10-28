# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0009_auto_20161027_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(default='upload/avatars/default-avatar.png', upload_to='upload/avatars/', blank=True, verbose_name='Votre avatar'),
        ),
    ]
