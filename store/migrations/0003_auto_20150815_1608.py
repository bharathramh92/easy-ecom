# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20150814_1727'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_auto_20150814_0124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('quantity', models.PositiveIntegerField()),
                ('added_or_updated_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Dispute',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('message', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=1, choices=[('PEN', 'Pending'), ('ACC', 'Accepted'), ('DEC', 'Declined')], default='PEN')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('price', models.DecimalField(max_digits=19, decimal_places=4)),
                ('currency', models.CharField(max_length=3)),
                ('total_available_stock', models.PositiveIntegerField()),
                ('total_sold', models.PositiveIntegerField()),
                ('available_countries', models.CharField(max_length=52)),
                ('domestic_shipping_company', models.CharField(max_length=100, blank=True, null=True)),
                ('domestic_shipping_cost', models.DecimalField(decimal_places=4, max_digits=19, blank=True, null=True)),
                ('free_domestic_shipping', models.BooleanField()),
                ('international_shipping_company', models.CharField(max_length=100, blank=True, null=True)),
                ('international_shipping_cost', models.DecimalField(decimal_places=4, max_digits=19, blank=True, null=True)),
                ('free_international_shipping', models.BooleanField()),
                ('local_pick_up_accepted', models.BooleanField()),
                ('dispatch_max_time', models.PositiveIntegerField()),
                ('return_accepted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('order_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
                ('brand', models.CharField(max_length=50)),
                ('shipping_product_dimension_height', models.DecimalField(max_digits=10, decimal_places=2)),
                ('shipping_product_dimension_width', models.DecimalField(max_digits=10, decimal_places=2)),
                ('shipping_product_dimension_length', models.DecimalField(max_digits=10, decimal_places=2)),
                ('shipping_product_dimension_units', models.CharField(max_length=2, choices=[('IN', 'Inches'), ('FT', 'Feet'), ('MM', 'Millimeters'), ('CM', 'Centimeters')], default='IN')),
                ('shipping_product_weight', models.DecimalField(max_digits=10, decimal_places=2)),
                ('shipping_product_weight_units', models.CharField(max_length=2, choices=[('OZ', 'Inches'), ('LB', 'Pounds'), ('MG', 'Milligrams'), ('G', 'Grams'), ('KG', 'Kilograms')], default='OZ')),
                ('posting_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated_datetime', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemFeedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('rating', models.PositiveSmallIntegerField()),
                ('description', models.CharField(max_length=500)),
                ('visibility', models.BooleanField(default=False)),
                ('posting_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated_datetime', models.DateTimeField(blank=True, null=True)),
                ('item', models.ForeignKey(to='store.Item', related_name='item_in_feedback')),
                ('user_reviewed', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user_item_review')),
            ],
        ),
        migrations.CreateModel(
            name='ItemMedia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('url', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=100, blank=True, null=True)),
                ('photo_or_video', models.CharField(max_length=1, choices=[('P', 'Photo'), ('V', 'Video')], default='P')),
                ('added_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('item', models.ForeignKey(to='store.Item', related_name='item_media')),
            ],
        ),
        migrations.CreateModel(
            name='MainSubCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('main_sub_category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tracking_number', models.CharField(max_length=30)),
                ('shipping_company', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField()),
                ('shipping_datetime', models.DateTimeField(blank=True, null=True)),
                ('delivery_datetime', models.DateTimeField(blank=True, null=True)),
                ('item_returned', models.NullBooleanField()),
                ('completed', models.BooleanField(default=False)),
                ('inventory', models.ForeignKey(to='store.Inventory', related_name='inventory_order')),
                ('invoice', models.ForeignKey(to='store.Invoice')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tax', models.DecimalField(max_digits=19, decimal_places=4)),
                ('total_amount_payed', models.DecimalField(max_digits=19, decimal_places=4)),
                ('payment_method', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SellingAddress',
            fields=[
                ('address_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, parent_link=True, to='accounts.Address')),
            ],
            bases=('accounts.address',),
        ),
        migrations.CreateModel(
            name='StoreName',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('store_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('sub_category_name', models.CharField(max_length=50)),
                ('category_fk', models.ForeignKey(to='store.StoreName')),
            ],
        ),
        migrations.RemoveField(
            model_name='customercontactseller',
            name='contacted_by',
        ),
        migrations.RemoveField(
            model_name='customercontactseller',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='discussionforcontactingseller',
            name='reply_for',
        ),
        migrations.RemoveField(
            model_name='discussionforcontactingseller',
            name='submitted_by',
        ),
        migrations.AddField(
            model_name='sellerfeedback',
            name='last_updated_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='CustomerContactSeller',
        ),
        migrations.DeleteModel(
            name='DiscussionForContactingSeller',
        ),
        migrations.AddField(
            model_name='mainsubcategory',
            name='sub_category_fk',
            field=models.ForeignKey(to='store.StoreName'),
        ),
        migrations.AddField(
            model_name='item',
            name='main_sub_category',
            field=models.ForeignKey(to='store.MainSubCategory', related_name='main_sub_cat_item'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment',
            field=models.OneToOneField(to='store.Payment'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='item',
            field=models.ForeignKey(to='store.Item', related_name='item_inventory'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='item_location',
            field=models.ForeignKey(to='store.SellingAddress', related_name='item_location_address'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='seller',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='seller_inventory'),
        ),
        migrations.AddField(
            model_name='dispute',
            name='order',
            field=models.ForeignKey(to='store.Order', related_name='order_no_disputes'),
        ),
        migrations.AddField(
            model_name='category',
            name='store_fk',
            field=models.ForeignKey(to='store.StoreName'),
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(to='store.Item', related_name='item_in_cart'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='cart_user'),
        ),
    ]
