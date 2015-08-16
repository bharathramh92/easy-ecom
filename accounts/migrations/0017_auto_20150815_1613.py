# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20150814_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userextended',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='userextended',
            name='profile_picture_url',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
    ]
