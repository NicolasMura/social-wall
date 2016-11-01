# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0016_auto_20161030_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(verbose_name='Post relatif', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_comments', blank=True, to='social.Post'),
        ),
    ]
