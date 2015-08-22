from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['category_name', 'description', 'parent_category']})
        ]
    list_display = ('category_name', 'parent_category')
admin.site.register(Category, CategoryAdmin)