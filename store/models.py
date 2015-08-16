from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from accounts.models import Address
# Create your models here.

#Categories
class StoreName(models.Model):
    store_name = models.CharField(max_length=50, null= False, blank= False)

    def __str__(self):
        return self.store_name

class Category(models.Model):
    category_name = models.CharField(max_length=50, null= False, blank= False)
    store_fk = models.ForeignKey(StoreName)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=50, null= False, blank= False)
    category_fk = models.ForeignKey(Category)

    def __str__(self):
        return self.sub_category_name

class MainSubCategory(models.Model):
    main_sub_category_name = models.CharField(max_length=50, null= False, blank= False)
    sub_category_fk = models.ForeignKey(SubCategory)

    def __str__(self):
        return self.main_sub_category_name

#items
class Item(models.Model):
    title = models.CharField(max_length=100, null= False, blank= False)
    description = models.CharField(max_length=2000, null= False, blank= False)
    brand = models.CharField(max_length=50, null= False, blank= False)

    shipping_product_dimension_height = models.DecimalField(max_digits=10, decimal_places= 2, null= False, blank= False)
    shipping_product_dimension_width = models.DecimalField(max_digits=10, decimal_places= 2, null= False, blank= False)
    shipping_product_dimension_length = models.DecimalField(max_digits=10, decimal_places= 2, null= False, blank= False)
    INCHES, FEET, MILLIMETERS, CENTIMETERS = "IN", "FT", "MM", "CM"
    DIMENSION_CHOICES = (
        (INCHES, 'Inches'),
        (FEET, 'Feet'),
        (MILLIMETERS, 'Millimeters'),
        (CENTIMETERS, 'Centimeters'),
    )
    shipping_product_dimension_units = models.CharField(max_length=2, choices=DIMENSION_CHOICES, default=INCHES, null= False, blank= False)

    shipping_product_weight = models.DecimalField(max_digits=10, decimal_places= 2, null= False, blank= False)
    OUNCES, POUNDS, MILLIGRAMS, GRAMS, KILOGRAMS = "OZ", "LB", "MG", "G", "KG"
    WEIGHT_CHOICES = (
        (OUNCES, 'Inches'),
        (POUNDS, 'Pounds'),
        (MILLIGRAMS, 'Milligrams'),
        (GRAMS, 'Grams'),
        (KILOGRAMS, 'Kilograms'),
    )
    shipping_product_weight_units = models.CharField(max_length=2, choices=WEIGHT_CHOICES, default=OUNCES, null= False, blank= False)

    main_sub_category = models.ManyToManyField(MainSubCategory, related_name= 'main_sub_cat_item')  #one item can be in multiple categories, but in a same store
    posting_datetime = models.DateTimeField(default = timezone.now, null= False, blank= False)
    last_updated_datetime = models.DateTimeField(null= True, blank= True)


class ItemMedia(models.Model):
    item = models.ForeignKey(Item, related_name= 'item_media')
    url = models.CharField(max_length=250, null= False, blank= False)
    title = models.CharField(max_length=100, null= True, blank= True)
    PHOTO, VIDEO = "P", "V"
    MEDIA_CHOICES = (
        (PHOTO, "Photo"),
        (VIDEO, "Video")
    )
    photo_or_video = models.CharField(max_length=1, choices=MEDIA_CHOICES, default=PHOTO, null= False, blank= False)
    added_datetime = models.DateTimeField(default = timezone.now, null= False, blank= False)

class SellingAddress(Address):                      #instead of using a additional boolean field for address in accounts in order to encapsulate accounts
    pass

class Inventory(models.Model):
    item = models.ForeignKey(Item, related_name= 'item_inventory')
    seller = models.ForeignKey(User, related_name= 'seller_inventory')

    price = models.DecimalField(max_digits=19, decimal_places= 4)
    currency = models.CharField(max_length=3)           #http://www.xe.com/iso4217.php use this to populate
    total_available_stock = models.PositiveIntegerField(null= False, blank= False)
    total_sold = models.PositiveIntegerField(null= False, blank= False)

    item_location = models.ForeignKey(SellingAddress, related_name= 'item_location_address')
    available_countries = models.CharField(max_length=52)             #origin country or worldwide

    domestic_shipping_company = models.CharField(max_length=100, null= True, blank= True)
    domestic_shipping_cost = models.DecimalField(max_digits=19, decimal_places= 4, null= True, blank= True)
    free_domestic_shipping = models.BooleanField(null= False, blank= False)

    international_shipping_company = models.CharField(max_length=100, null= True, blank= True)
    international_shipping_cost = models.DecimalField(max_digits=19, decimal_places= 4, null= True, blank= True)
    free_international_shipping = models.BooleanField(null= False, blank= False)

    local_pick_up_accepted = models.BooleanField(null= False, blank= False)

    dispatch_max_time = models.PositiveIntegerField()                      #in hours
    return_accepted = models.BooleanField(null= False, blank= False)

    listing_end_datetime = models.DateTimeField(default= timezone.now, null= False, blank= False)

#remaining details are pending
class Payment(models.Model):
    tax = models.DecimalField(max_digits=19, decimal_places= 4)
    total_amount_payed = models.DecimalField(max_digits=19, decimal_places= 4)
    payment_method = models.CharField(max_length=50)

class Invoice(models.Model):
    payment = models.OneToOneField(Payment)
    order_datetime = models.DateTimeField(default = timezone.now)

class Order(models.Model):
    inventory = models.ForeignKey(Inventory, related_name= 'inventory_order')
    tracking_number = models.CharField(max_length=30, null= False, blank= False)
    shipping_company = models.CharField(max_length=50, null= False, blank= False)

    quantity = models.PositiveIntegerField(null= False, blank= False)
    shipping_datetime = models.DateTimeField(null= True, blank= True)
    delivery_datetime = models.DateTimeField(null= True, blank= True)

    item_returned = models.NullBooleanField()
    completed = models.BooleanField(default= False, null= False, blank= False)

    invoice = models.ForeignKey(Invoice)

class Dispute(models.Model):
    order = models.ForeignKey(Order, related_name="order_no_disputes")
    message = models.CharField(max_length=1000, null= False, blank= False)
    ACCEPTED, DECLINED, PENDING = "ACC", "DEC", "PEN"
    DISPUTE_STATUS_CHOICES = (
        (PENDING, "Pending"),
        (ACCEPTED, "Accepted"),
        (DECLINED, "Declined")
    )
    status = models.CharField(max_length=1, choices=DISPUTE_STATUS_CHOICES, default= PENDING, null= False, blank= False)

class Cart(models.Model):
    item = models.ForeignKey(Item, related_name= "item_in_cart")
    quantity = models.PositiveIntegerField(null= False, blank= False)
    user = models.ForeignKey(User, related_name="cart_user")
    added_or_updated_datetime = models.DateTimeField(default = timezone.now)

class ContactUs(models.Model):
    email = models.EmailField(null= False, blank= False)
    subject = models.CharField(max_length=50, null= False, blank= False)
    description = models.CharField(max_length=1000, null= False, blank= False)

class ItemFeedback(models.Model):
    user_reviewed = models.ForeignKey(User, related_name= "user_item_review")
    item = models.ForeignKey(Item, related_name= 'item_in_feedback')
    rating = models.PositiveSmallIntegerField(null= False, blank= False)
    description = models.CharField(max_length=500, null= False, blank= False)
    visibility = models.BooleanField(default= False, null= False, blank= False)
    posting_datetime = models.DateTimeField(default =  timezone.now)
    last_updated_datetime = models.DateTimeField(null= True, blank= True)

#seller feedback
class SellerFeedback(models.Model):
    reviewer = models.ForeignKey(User, related_name= 'reviewed_by')
    seller = models.ForeignKey(User, related_name= 'seller')
    review_description = models.CharField(max_length=1000, null= False, blank= False)
    review_points = models.PositiveSmallIntegerField(null= False, blank= False)
    posting_datetime = models.DateTimeField(default = timezone.now)
    last_updated_datetime = models.DateTimeField(null= True, blank= True)