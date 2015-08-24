# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20150823_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstore',
            name='Language',
            field=models.CharField(choices=[('eng', 'English'), ('fre', 'French')], max_length=3, default='eng'),
        ),
    ]
