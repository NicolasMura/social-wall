# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0014_auto_20161125_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(default='static/avatars/default-avatar.png', blank=True, verbose_name='Votre avatar', upload_to='upload/avatars'),
        ),
    ]
