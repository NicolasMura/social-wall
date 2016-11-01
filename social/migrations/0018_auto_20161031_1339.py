# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0017_auto_20161030_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(verbose_name='Posts relatifs', to='social.Comment', related_name='comments'),
        ),
    ]
