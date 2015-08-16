# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_inventory_listing_end_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainsubcategory',
            name='sub_category_fk',
            field=models.ForeignKey(to='store.SubCategory'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category_fk',
            field=models.ForeignKey(to='store.Category'),
        ),
    ]
