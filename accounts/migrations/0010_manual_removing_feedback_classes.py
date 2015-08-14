# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_forgotpasswordverification'),

    ]

    operations = [
    # migrations.DeleteModel("SellerFeedback"),
    # migrations.DeleteModel("CustomerContactSeller"),
    migrations.DeleteModel("DiscussionForContactingSeller"),
    ]
