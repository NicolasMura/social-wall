# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0015_auto_20161125_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(blank=True, default='media/avatars/default-avatar.png', verbose_name='Votre avatar', upload_to='upload/avatars'),
        ),
    ]
