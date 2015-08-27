# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20150827_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='brand',
        ),
    ]
