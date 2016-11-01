# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0014_auto_20161028_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('content', models.CharField(verbose_name='Commentaire', max_length=3000)),
                ('submit_date', models.DateTimeField(auto_now_add=True, verbose_name='date/time submitted')),
                ('is_public', models.BooleanField(default=True, verbose_name='is public', help_text='Uncheck this box to make the comment effectively disappear from the site.')),
                ('is_removed', models.BooleanField(default=False, verbose_name='is removed', help_text='Check this box if the comment is inappropriate. A "This comment has been removed" message will be displayed instead.')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='social.Post', related_name='comment_comments', blank=True, null=True, verbose_name='Commentaire')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, related_name='comment_comments', blank=True, null=True, verbose_name='Profil')),
            ],
            options={
                'verbose_name': 'Commentaire utilisateur',
                'verbose_name_plural': 'Commentaires utilisateur',
            },
        ),
    ]
