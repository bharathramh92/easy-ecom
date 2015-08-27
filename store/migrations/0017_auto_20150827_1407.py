# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20150827_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='total_sold',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
