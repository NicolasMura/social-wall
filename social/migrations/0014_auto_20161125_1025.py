# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0013_auto_20161123_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(upload_to='upload/avatars', verbose_name='Votre avatar', blank=True, default='avatars/default-avatar.png'),
        ),
    ]
