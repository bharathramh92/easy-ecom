# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_auto_20151008_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemaddress',
            name='address',
        ),
        migrations.RemoveField(
            model_name='itemaddress',
            name='address_ptr',
        ),
        migrations.AlterField(
            model_name='inventory',
            name='item_location',
            field=models.ForeignKey(related_name='item_location_address', to='accounts.Address'),
        ),
        migrations.DeleteModel(
            name='ItemAddress',
        ),
    ]
