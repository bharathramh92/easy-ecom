from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
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