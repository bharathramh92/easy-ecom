from django.contrib import admin

# Register your models here.
from .models import *

class DiscussionForContactingSellerInline(admin.StackedInline):
    model = DiscussionForContactingSeller
    extra = 1


class CustomerContactSellerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['contacted_by', 'seller']}),
        ('Message', {'fields': ['subject', 'message', 'posting_datetime']}),
    ]
    inlines = [DiscussionForContactingSellerInline]
    list_display = ('contacted_by', 'seller', 'subject', 'posting_datetime')

admin.site.register(CustomerContactSeller, CustomerContactSellerAdmin)
admin.site.register(SellerFeedback)