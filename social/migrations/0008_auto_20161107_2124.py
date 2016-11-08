# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_auto_20161107_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='wall_profile',
            new_name='to_wall_profile',
        ),
    ]
