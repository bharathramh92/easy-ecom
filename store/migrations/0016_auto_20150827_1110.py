# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_remove_item_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookstore',
            name='book_condition',
        ),
        migrations.RemoveField(
            model_name='bookstore',
            name='book_type',
        ),
        migrations.AddField(
            model_name='inventory',
            name='condition',
            field=models.CharField(default='n', max_length=1),
        ),
    ]
