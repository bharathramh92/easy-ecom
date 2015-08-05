from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Address)
admin.site.register(UserExtended)
admin.site.register(EmailVerification)
admin.site.register(SellerFeedback)
admin.site.register(CustomerContactSeller)
admin.site.register(SellerReplyForContacting)