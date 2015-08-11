# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20150805_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country_code_phone_number',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='userextended',
            name='country_code_phone_number',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='userextended',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
