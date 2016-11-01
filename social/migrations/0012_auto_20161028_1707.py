# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0011_auto_20161027_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('content', models.TextField(max_length=3000, verbose_name='Commentaire')),
                ('submit_date', models.DateTimeField(verbose_name='date/time submitted', auto_now_add=True)),
                ('is_public', models.BooleanField(default=True, help_text='Uncheck this box to make the comment effectively disappear from the site.', verbose_name='is public')),
                ('is_removed', models.BooleanField(default=False, help_text='Check this box if the comment is inappropriate. A "This comment has been removed" message will be displayed instead.', verbose_name='is removed')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='commentprofile_comments', blank=True, verbose_name='Profil', on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'verbose_name': "Post d'un utilisateur",
            },
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
