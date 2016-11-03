# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import social.models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(verbose_name='Commentaire', default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(verbose_name='Commentaire', default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(verbose_name='Votre avatar', default='upload/avatars/default-avatar.png', upload_to='upload/avatars', blank=True),
        ),
    ]
