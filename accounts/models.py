from django.db import models
from django.contrib.auth.models import User
from ecom_functions import random_alphanumeric
from constants.constants import *
from django.utils import timezone
import datetime

# Create your models here.
class Address(models.Model):
    contact_name = models.CharField(max_length=100)
    country_name = models.CharField(max_length=50)
    city_name = models.CharField(max_length=50)
    state_name = models.CharField(max_length=50)
    street_address_line_1 = models.CharField(max_length= 60)
    street_address_line_2 = models.CharField(max_length= 60)
    phone_number = models.CharField(max_length = 15)
    country_code_phone_number = models.CharField(max_length = 5)
    added_datetime = models.DateTimeField(null=True , blank= True)
    last_updated_datetime = models.DateTimeField(null=True , blank= True)
    user = models.ForeignKey(User, null= True)

class UserExtended(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.CharField(max_length=100)
    last_updated_profile_picture_datetime = models.DateTimeField(null=True , blank= True)
    phone_number = models.CharField(max_length = 15)
    country_code_phone_number = models.CharField(max_length = 5)
    is_email_verified = models.BooleanField(default=False)
    email_verified_datetime = models.DateTimeField(null=True , blank= True)
    is_phone_number_verified = models.BooleanField(default=False)
    phone_number_verified_datetime = models.DateTimeField(null=True , blank= True)
    phone_number_updated_datetime = models.DateTimeField(null=True , blank= True)
    selling_enabled = models.BooleanField(default= False)

class EmailVerification(models.Model):
    user = models.ForeignKey(User)
    verification_code = models.CharField(max_length=120)
    sent_datetime = models.DateTimeField(default =  timezone.now)
    def is_not_expired(self):           #true if not expired. Taken care for future questions as well
        now = timezone.now()
        return now - datetime.timedelta(days = EMAIL_VERIFICATION_EXPIRATION_DAYS) < self.sent_datetime < now

class SellerFeedback(models.Model):
    reviewer = models.ForeignKey(User, related_name= 'reviewed_by')
    seller = models.ForeignKey(User, related_name= 'seller')
    review_description = models.CharField(max_length=1000)
    review_points = models.PositiveSmallIntegerField()
    posting_datetime = models.DateTimeField(default =  timezone.now)

class CustomerContactSeller(models.Model):
    contacted_by = models.ForeignKey(User, related_name= 'contacted_by')
    seller = models.ForeignKey(User, related_name= 'seller_contact')
    subject = models.CharField(max_length=80)
    message = models.CharField(max_length=1000)
    posting_datetime = models.DateTimeField(default =  timezone.now)

class SellerReplyForContacting(models.Model):
    reply_for = models.ForeignKey(CustomerContactSeller, related_name= 'reply_for_customer_contact')
    message = models.CharField(max_length=1000)
    posting_datetime = models.DateTimeField(default =  timezone.now)