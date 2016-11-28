# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0017_auto_20161125_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default='', max_length=1000, verbose_name='Commentaire'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_public',
            field=models.BooleanField(default=True, help_text='Uncheck this box to make the comment effectively disappear from the site.', verbose_name='publique ?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='', max_length=1000, verbose_name='Commentaire'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(default=True, help_text='Uncheck this box to make the comment effectively disappear from the site.', verbose_name='publique ?'),
        ),
    ]
