from django.db import models
from django.contrib.auth.models import User
from . import constants
from django.utils import timezone
import datetime

# Create your models here.
class UserExtended(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.CharField(max_length=100, null= True, blank= True)
    last_updated_profile_picture_datetime = models.DateTimeField(null=True , blank= True)
    MALE, FEMALE = "M", "F"
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female")
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null= True, blank= True)
    phone_number = models.CharField(max_length = 15, null= True, blank= True)
    country_code_phone_number = models.CharField(max_length = 5, null= True, blank= True)
    is_email_verified = models.BooleanField(default=False)
    email_verified_datetime = models.DateTimeField(null=True , blank= True)
    is_phone_number_verified = models.BooleanField(default=False)
    phone_number_verified_datetime = models.DateTimeField(null=True , blank= True)
    phone_number_updated_datetime = models.DateTimeField(null=True , blank= True)
    selling_enabled = models.BooleanField(default= False)
    last_updated_password_datetime = models.DateTimeField(null=True , blank= True)

class Address(models.Model):
    contact_name = models.CharField(max_length=100, null= False)
    country_name = models.CharField(max_length=52, null= False)
    city_name = models.CharField(max_length=50, null= False)
    state_name = models.CharField(max_length=50, null= False)
    street_address_line_1 = models.CharField(max_length= 60, null= False)
    street_address_line_2 = models.CharField(max_length= 60, null= True)
    zipcode = models.CharField(max_length=32, null=False)
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
        return now - datetime.timedelta(days = constants.EMAIL_VERIFICATION_EXPIRATION_DAYS) < self.sent_datetime < now

class ForgotPasswordVerification(models.Model):
    user = models.ForeignKey(User)
    verification_code = models.CharField(max_length=120)
    sent_datetime = models.DateTimeField(default =  timezone.now)

    def is_not_expired_forgot_password(self):           #true if not expired. Taken care for future time as well(would return false).
        now = timezone.now()
        return now - datetime.timedelta(days = constants.FORGOT_PASSWORD_EXPIRATION_DAYS) < self.sent_datetime < now
