# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerContactSeller',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('subject', models.CharField(max_length=80)),
                ('message', models.CharField(max_length=1000)),
                ('posting_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('contacted_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='contacted_by')),
                ('seller', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='seller_contact')),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionForContactingSeller',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('message', models.CharField(max_length=1000)),
                ('posting_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('reply_for', models.ForeignKey(to='store.CustomerContactSeller', related_name='reply_for_customer_contact')),
                ('submitted_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='submitted_by_user')),
            ],
        ),
        migrations.CreateModel(
            name='SellerFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('review_description', models.CharField(max_length=1000)),
                ('review_points', models.PositiveSmallIntegerField()),
                ('posting_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('reviewer', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='reviewed_by')),
                ('seller', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='seller')),
            ],
        ),
    ]
