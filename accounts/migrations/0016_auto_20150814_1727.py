# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_userextended_photo_or_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userextended',
            old_name='photo_or_video',
            new_name='gender',
        ),
    ]
