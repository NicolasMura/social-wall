# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0015_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'Commentaires', 'verbose_name': 'Commentaire'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Posts', 'verbose_name': 'Post'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': 'Profils utilisateurs', 'verbose_name': 'Profil utilisateur'},
        ),
    ]
