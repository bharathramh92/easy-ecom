# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20150831_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstore',
            name='isbn_13',
            field=models.CharField(unique=True, max_length=13),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='condition',
            field=models.CharField(max_length=1, default='n', choices=[('n', 'New'), ('u', 'Used')]),
        ),
    ]
