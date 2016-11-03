# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20161102_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='wall_profile',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Mur sur lequel le post a été publié', default=1, related_name='wall_profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Profil', default=1, related_name='comment_comments'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Profil', default=1, related_name='post_comments'),
            preserve_default=False,
        ),
    ]
