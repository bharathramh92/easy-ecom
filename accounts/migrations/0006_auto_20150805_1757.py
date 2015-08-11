# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20150805_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(to='accounts.UserExtended'),
        ),
        migrations.AlterField(
            model_name='userextended',
            name='country_code_phone_number',
            field=models.CharField(max_length=5, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userextended',
            name='phone_number',
            field=models.CharField(max_length=15, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userextended',
            name='profile_picture',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
