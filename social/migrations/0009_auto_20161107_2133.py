# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_auto_20161107_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='to_wall_profile',
        ),
        migrations.AddField(
            model_name='post',
            name='wall',
            field=models.ForeignKey(verbose_name='Publié sur le mur de', related_name='wall', to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_public',
            field=models.BooleanField(verbose_name='public ?', help_text='Uncheck this box to make the comment effectively disappear from the site.', default=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_removed',
            field=models.BooleanField(verbose_name='Désactivé ?', help_text='Check this box if the comment is inappropriate. A "This comment has been removed" message will be displayed instead.', default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='submit_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de publication'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(verbose_name='public ?', help_text='Uncheck this box to make the comment effectively disappear from the site.', default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_removed',
            field=models.BooleanField(verbose_name='Désactivé ?', help_text='Check this box if the comment is inappropriate. A "This comment has been removed" message will be displayed instead.', default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='submit_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de publication'),
        ),
    ]
