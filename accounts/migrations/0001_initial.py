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
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=100)),
                ('country_name', models.CharField(max_length=50)),
                ('city_name', models.CharField(max_length=50)),
                ('state_name', models.CharField(max_length=50)),
                ('street_address_line_1', models.CharField(max_length=60)),
                ('street_address_line_2', models.CharField(max_length=60)),
                ('phone_number', models.CharField(max_length=15)),
                ('country_code_phone_number', models.CharField(max_length=5)),
                ('added_datetime', models.DateTimeField(null=True, blank=True)),
                ('last_updated_datetime', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailVerification',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('verification_code', models.CharField(max_length=120)),
                ('sent_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SellerFeedback',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('review_description', models.CharField(max_length=1000)),
                ('review_points', models.PositiveSmallIntegerField()),
                ('reviewer', models.ForeignKey(related_name='reviewed_by', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddressRelation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('address', models.ForeignKey(to='accounts.Address')),
            ],
        ),
        migrations.CreateModel(
            name='UserExtended',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('profile_picture', models.CharField(max_length=100)),
                ('last_updated_profile_picture_datetime', models.DateTimeField(null=True, blank=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('country_code_phone_number', models.CharField(max_length=5)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_phone_number_verified', models.BooleanField(default=False)),
                ('phone_number_updated_datetime', models.DateTimeField(null=True, blank=True)),
                ('addresses', models.ManyToManyField(through='accounts.UserAddressRelation', to='accounts.Address')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='useraddressrelation',
            name='user_extended',
            field=models.ForeignKey(to='accounts.UserExtended'),
        ),
    ]
