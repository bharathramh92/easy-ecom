# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('store', '0009_auto_20150819_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='store_fk',
        ),
        migrations.RemoveField(
            model_name='mainsubcategory',
            name='sub_category_fk',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category_fk',
        ),
        migrations.RemoveField(
            model_name='item',
            name='main_sub_category',
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ManyToManyField(related_name='main_sub_cat_item', to='categories.Category'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='MainSubCategory',
        ),
        migrations.DeleteModel(
            name='StoreName',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
