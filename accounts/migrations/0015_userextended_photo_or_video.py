# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20150814_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextended',
            name='photo_or_video',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], blank=True, max_length=1, null=True),
        ),
    ]
