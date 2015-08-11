# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_auto_20150805_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerreplyforcontacting',
            name='submitted_by',
            field=models.ForeignKey(default=1, related_name='submitted_by_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
