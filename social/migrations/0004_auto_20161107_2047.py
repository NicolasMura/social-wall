# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20161107_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(verbose_name='Auteur', related_name='comment_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(verbose_name='Auteur', related_name='post_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(verbose_name='Commentaires relatifs', related_name='comments', blank=True, to='social.Comment', null=True),
        ),
    ]
