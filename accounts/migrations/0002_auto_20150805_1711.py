# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerContactSeller',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('subject', models.CharField(max_length=80)),
                ('message', models.CharField(max_length=1000)),
                ('posting_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('contacted_by', models.ForeignKey(related_name='contacted_by', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(related_name='seller_contact', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SellerReplyForContacting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('message', models.CharField(max_length=1000)),
                ('posting_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('reply_for', models.ForeignKey(related_name='reply_for_customer_contact', to='accounts.CustomerContactSeller')),
            ],
        ),
        migrations.AddField(
            model_name='sellerfeedback',
            name='posting_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='userextended',
            name='email_verified_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userextended',
            name='phone_number_verified_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userextended',
            name='selling_enabled',
            field=models.BooleanField(default=False),
        ),
    ]
