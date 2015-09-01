# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_inventory_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstore',
            name='isbn_10',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]
