# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20150824_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellingaddress',
            name='address_ptr',
        ),
        migrations.AlterField(
            model_name='inventory',
            name='available_countries',
            field=models.CharField(max_length=12, default='Worldwide', choices=[('Domestic', 'Domestic'), ('Worldwide', 'Worldwide')]),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='currency',
            field=models.CharField(max_length=3, default='USD'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='item_location',
            field=models.ForeignKey(related_name='item_location_address', to='accounts.Address'),
        ),
        migrations.DeleteModel(
            name='SellingAddress',
        ),
    ]
