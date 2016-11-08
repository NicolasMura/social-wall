# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='social.Post', verbose_name='Post relatif', related_name='comment_comments'),
        ),
        migrations.AlterField(
            model_name='post',
            name='wall_profile',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Mur sur lequel le post a été publié', related_name='wall_profile'),
        ),
    ]
