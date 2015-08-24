# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20150824_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookstore',
            old_name='Language',
            new_name='language',
        ),
    ]
