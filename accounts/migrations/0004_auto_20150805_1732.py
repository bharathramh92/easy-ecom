# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150805_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='added_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='address',
            name='country_code_phone_number',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_address_line_2',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userextended',
            name='profile_picture',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
