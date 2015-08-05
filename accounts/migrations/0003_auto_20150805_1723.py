# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20150805_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddressrelation',
            name='address',
        ),
        migrations.RemoveField(
            model_name='useraddressrelation',
            name='user_extended',
        ),
        migrations.RemoveField(
            model_name='userextended',
            name='addresses',
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.DeleteModel(
            name='UserAddressRelation',
        ),
    ]
