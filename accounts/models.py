from django.db import models
from django.contrib.auth.models import User
from ecom_functions import random_alphanumeric
from constants.constants import *
from django.utils import timezone
import datetime

# Create your models here.

class UserExtended(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.CharField(max_length=100, null= True, blank= True)
    last_updated_profile_picture_datetime = models.DateTimeField(null=True , blank= True)
    phone_number = models.CharField(max_length = 15, null= True, blank= True)
    country_code_phone_number = models.CharField(max_length = 5, null= True, blank= True)
    is_email_verified = models.BooleanField(default=False)
    email_verified_datetime = models.DateTimeField(null=True , blank= True)
    is_phone_number_verified = models.BooleanField(default=False)
    phone_number_verified_datetime = models.DateTimeField(null=True , blank= True)
    phone_number_updated_datetime = models.DateTimeField(null=True , blank= True)
    selling_enabled = models.BooleanField(default= False)


class Address(models.Model):
    contact_name = models.CharField(max_length=100, null= False)
    country_name = models.CharField(max_length=50, null= False)
    city_name = models.CharField(max_length=50, null= False)
    state_name = models.CharField(max_length=50, null= False)
    street_address_line_1 = models.CharField(max_length= 60, null= False)
    street_address_line_2 = models.CharField(max_length= 60, null= True)
    phone_number = models.CharField(max_length = 15, null= False)
    country_code_phone_number = models.CharField(max_length = 5, null= False)
    added_datetime = models.DateTimeField(default= timezone.now)
    last_updated_datetime = models.DateTimeField(null=True , blank= True)
    user = models.ForeignKey(UserExtended)

    def __str__(self):
        return self.contact_name + self.street_address_line_1 + self.city_name + self.country_name

class EmailVerification(models.Model):
    user = models.ForeignKey(User)
    verification_code = models.CharField(max_length=120)
    sent_datetime = models.DateTimeField(default =  timezone.now)

    def is_not_expired_email_verification(self):           #true if not expired. Taken care for future time as well(would return false).
        now = timezone.now()
        return now - datetime.timedelta(days = EMAIL_VERIFICATION_EXPIRATION_DAYS) < self.sent_datetime < now

    def is_not_expired_forgot_password(self):           #true if not expired. Taken care for future time as well(would return false).
        now = timezone.now()
        return now - datetime.timedelta(days = FORGOT_PASSWORD_EXPIRATION_DAYS) < self.sent_datetime < now


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

class DiscussionForContactingSeller(models.Model):
    reply_for = models.ForeignKey(CustomerContactSeller, related_name= 'reply_for_customer_contact')
    message = models.CharField(max_length=1000)
    submitted_by = models.ForeignKey(User, related_name= 'submitted_by_user')
    posting_datetime = models.DateTimeField(default =  timezone.now)