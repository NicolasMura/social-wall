# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_auto_20161107_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Post relatif', blank=True, related_name='comment_comments', null=True, to='social.Post'),
        ),
    ]
