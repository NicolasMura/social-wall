# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings
import django.db.models.deletion
import django.utils.timezone
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(max_length=30, verbose_name='username', help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], error_messages={'unique': 'A user with that username already exists.'})),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=254, blank=True)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', verbose_name='staff status', default=False)),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('avatar', models.FileField(verbose_name='Votre avatar', upload_to='upload/avatars', default='upload/avatars/default-avatar.png', blank=True)),
                ('groups', models.ManyToManyField(to='auth.Group', related_name='user_set', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', blank=True)),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', related_name='user_set', related_query_name='user', help_text='Specific permissions for this user.', verbose_name='user permissions', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Profils utilisateurs',
                'verbose_name': 'Profil utilisateur',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('content', models.CharField(verbose_name='Commentaire', max_length=3000)),
                ('submit_date', models.DateTimeField(verbose_name='date/time submitted', auto_now_add=True)),
                ('is_public', models.BooleanField(help_text='Uncheck this box to make the comment effectively disappear from the site.', verbose_name='is public', default=True)),
                ('is_removed', models.BooleanField(help_text='Check this box if the comment is inappropriate. A "This comment has been removed" message will be displayed instead.', verbose_name='is removed', default=False)),
                ('user', models.ForeignKey(related_name='comment_comments', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Profil', to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Commentaires',
                'verbose_name': 'Commentaire',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('content', models.CharField(verbose_name='Commentaire', max_length=3000)),
                ('submit_date', models.DateTimeField(verbose_name='date/time submitted', auto_now_add=True)),
                ('is_public', models.BooleanField(help_text='Uncheck this box to make the comment effectively disappear from the site.', verbose_name='is public', default=True)),
                ('is_removed', models.BooleanField(help_text='Check this box if the comment is inappropriate. A "This comment has been removed" message will be displayed instead.', verbose_name='is removed', default=False)),
                ('comments', models.ManyToManyField(verbose_name='Commentaires relatifs', related_name='comments', to='social.Comment')),
                ('user', models.ForeignKey(related_name='post_comments', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Profil', to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Posts',
                'verbose_name': 'Post',
            },
        ),
    ]
