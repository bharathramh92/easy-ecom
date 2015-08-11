# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_sellerreplyforcontacting_submitted_by'),
    ]

    operations = [
        migrations.RenameModel('SellerReplyForContacting', 'DiscussionForContactingSeller')
    ]
