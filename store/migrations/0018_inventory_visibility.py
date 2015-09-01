# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20150827_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='visibility',
            field=models.BooleanField(default=True),
        ),
    ]
