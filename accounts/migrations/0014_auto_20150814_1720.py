# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_address_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country_name',
            field=models.CharField(max_length=52),
        ),
    ]
