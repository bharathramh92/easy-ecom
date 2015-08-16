from django.contrib import admin

# Register your models here.
from .models import *

class AddressInline(admin.StackedInline):
    model = Address
    extra = 1

class UserExtendedAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['user', 'last_updated_password_datetime']}),
        ('Profile Picture', {'fields': ['profile_picture', 'last_updated_profile_picture_datetime']}),
        ('Phone Number', {'fields': ['country_code_phone_number', 'phone_number', 'is_phone_number_verified', 'phone_number_verified_datetime', 'phone_number_updated_datetime']}),
        ('Email verification', {'fields': ['is_email_verified', 'email_verified_datetime']}),
    ]
    inlines = [AddressInline]
    list_display = ('user',)

admin.site.register(UserExtended, UserExtendedAdmin)
admin.site.register(EmailVerification)
admin.site.register(ForgotPasswordVerification)