# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20161022_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(blank=True, upload_to='static/avatars/', null=True, default='static/avatars/default-icon.png', verbose_name='Votre avatar'),
        ),
    ]
