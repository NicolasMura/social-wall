# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_auto_20161107_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='wall_profile',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, related_name='wall_profile', verbose_name='Mur sur lequel le post a été publié'),
        ),
    ]
