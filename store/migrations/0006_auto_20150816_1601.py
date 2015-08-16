# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20150815_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='main_sub_category',
        ),
        migrations.AddField(
            model_name='item',
            name='main_sub_category',
            field=models.ManyToManyField(to='store.MainSubCategory', related_name='main_sub_cat_item'),
        ),
    ]
