# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20150816_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstore',
            name='item',
            field=models.OneToOneField(related_name='book_store_item', to='store.Item'),
        ),
    ]
