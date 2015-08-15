# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_userextended_last_updated_password_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zipcode',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
    ]
