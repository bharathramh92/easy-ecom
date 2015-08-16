# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20150816_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(null=True, max_length=1000, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookStore',
            fields=[
                ('isbn_10', models.CharField(max_length=10)),
                ('isbn_13', models.CharField(primary_key=True, max_length=13, serialize=False)),
                ('Language', models.CharField(max_length=50)),
                ('book_type', models.CharField(choices=[('H', 'Hardcover'), ('P', 'Paperback')], default='H', max_length=1)),
                ('book_condition', models.CharField(choices=[('U', 'Used'), ('N', 'New')], default='N', max_length=1)),
                ('authors', models.ManyToManyField(to='store.Author')),
                ('item', models.ForeignKey(related_name='book_store_item', to='store.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(null=True, max_length=1000, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('contact_email', models.EmailField(null=True, max_length=254, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='bookstore',
            name='publisher',
            field=models.ForeignKey(to='store.Publisher'),
        ),
    ]
