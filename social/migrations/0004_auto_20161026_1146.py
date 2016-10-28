# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20161026_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(blank=True, verbose_name='Votre avatar', upload_to='upload/avatars/', null=True, default='upload/avatars/default-icon.png'),
        ),
    ]
