# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20150816_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='shipping_product_weight_units',
            field=models.CharField(default='OZ', max_length=2, choices=[('OZ', 'Ounces'), ('LB', 'Pounds'), ('MG', 'Milligrams'), ('G', 'Grams'), ('KG', 'Kilograms')]),
        ),
    ]
