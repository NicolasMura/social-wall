# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0012_auto_20161118_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(blank=True, verbose_name='Votre avatar', upload_to='upload/avatars', default='static/avatars/default-avatar.png'),
        ),
    ]
