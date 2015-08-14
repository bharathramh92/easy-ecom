# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_manual_removing_feedback_classes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customercontactseller',
            name='contacted_by',
        ),
        migrations.RemoveField(
            model_name='customercontactseller',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='sellerfeedback',
            name='reviewer',
        ),
        migrations.RemoveField(
            model_name='sellerfeedback',
            name='seller',
        ),
        migrations.DeleteModel(
            name='CustomerContactSeller',
        ),
        migrations.DeleteModel(
            name='SellerFeedback',
        ),
    ]
