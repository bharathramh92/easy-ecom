from django.contrib import admin
from store.models import *

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'description', 'website', 'created_by',]}),
    ]
    list_display = ('name', 'created_by')

admin.site.register(Author, AuthorAdmin)