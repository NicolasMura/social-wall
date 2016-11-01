# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0012_auto_20161028_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('content', models.TextField(verbose_name='Commentaire', max_length=3000)),
                ('submit_date', models.DateTimeField(verbose_name='date/time submitted', auto_now_add=True)),
                ('is_public', models.BooleanField(help_text='Uncheck this box to make the comment effectively disappear from the site.', verbose_name='is public', default=True)),
                ('is_removed', models.BooleanField(help_text='Check this box if the comment is inappropriate. A "This comment has been removed" message will be displayed instead.', verbose_name='is removed', default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='post_comments', to=settings.AUTH_USER_MODEL, blank=True, verbose_name='Profil', null=True)),
            ],
            options={
                'verbose_name_plural': 'Posts utilisateur',
                'verbose_name': 'Post utilisateur',
            },
        ),
        migrations.RemoveField(
            model_name='commentprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='CommentProfile',
        ),
    ]
