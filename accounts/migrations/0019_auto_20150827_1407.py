# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_remove_userextended_selling_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='street_address_line_2',
            field=models.CharField(blank=True, null=True, max_length=60),
        ),
    ]
