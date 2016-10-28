# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.contrib.auth.models
from django.conf import settings
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(max_length=30, verbose_name='username', error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], unique=True)),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('avatar', models.ImageField(verbose_name='Votre avatar', null=True, upload_to='avatars/', blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', to='auth.Group', related_name='user_set', blank=True)),
                ('user_permissions', models.ManyToManyField(related_query_name='user', help_text='Specific permissions for this user.', verbose_name='user permissions', to='auth.Permission', related_name='user_set', blank=True)),
            ],
            options={
                'verbose_name': 'Profil',
                'verbose_name_plural': 'Profils',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('content', models.TextField(max_length=3000, verbose_name='Commentaire')),
                ('submit_date', models.DateTimeField(verbose_name='date/time submitted', auto_now_add=True)),
                ('is_public', models.BooleanField(verbose_name='is public', help_text='Uncheck this box to make the comment effectively disappear from the site.', default=True)),
                ('is_removed', models.BooleanField(verbose_name='is removed', help_text='Check this box if the comment is inappropriate. A "This comment has been removed" message will be displayed instead.', default=False)),
                ('user', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL, null=True, related_name='comment_comments', on_delete=django.db.models.deletion.SET_NULL, blank=True)),
            ],
            options={
                'verbose_name': 'Commentaire',
            },
        ),
    ]
