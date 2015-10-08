# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20150827_1407'),
        ('store', '0020_auto_20151008_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemAddress',
            fields=[
                ('address_ptr', models.OneToOneField(parent_link=True, primary_key=True, auto_created=True, serialize=False, to='accounts.Address')),
                ('address', models.ForeignKey(related_name='item_location_address', to='accounts.Address')),
            ],
            bases=('accounts.address',),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='item_location',
            field=models.ForeignKey(related_name='item_location_address_inventory', to='store.ItemAddress'),
        ),
    ]
