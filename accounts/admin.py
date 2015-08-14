from django.contrib import admin

# Register your models here.
from .models import *

class AddressInline(admin.StackedInline):
    model = Address
    extra = 1

# class DiscussionForContactingSellerInline(admin.StackedInline):
#     model = DiscussionForContactingSeller
#     extra = 1

class UserExtendedAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['user', 'selling_enabled']}),
        ('Profile Picture', {'fields': ['profile_picture', 'last_updated_profile_picture_datetime']}),
        ('Phone Number', {'fields': ['country_code_phone_number', 'phone_number', 'is_phone_number_verified', 'phone_number_verified_datetime', 'phone_number_updated_datetime']}),
        ('Email verification', {'fields': ['is_email_verified', 'email_verified_datetime']}),
    ]
    inlines = [AddressInline]
    list_display = ('user', 'selling_enabled')

# class CustomerContactSellerAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['contacted_by', 'seller']}),
#         ('Message', {'fields': ['subject', 'message', 'posting_datetime']}),
#     ]
#     inlines = [DiscussionForContactingSellerInline]
#     list_display = ('contacted_by', 'seller', 'subject', 'posting_datetime')

admin.site.register(UserExtended, UserExtendedAdmin)
# admin.site.register(CustomerContactSeller, CustomerContactSellerAdmin)
admin.site.register(EmailVerification)
admin.site.register(ForgotPasswordVerification)
# admin.site.register(SellerFeedback)