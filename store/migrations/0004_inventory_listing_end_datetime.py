# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20150815_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='listing_end_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
