# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20150813_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextended',
            name='last_updated_password_datetime',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
