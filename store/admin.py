from django.contrib import admin

# Register your models here.
from .models import *

class MainSubCategoryInline(admin.StackedInline):
    model = MainSubCategory
    extra = 1

class SubCatInline(admin.StackedInline):
    model = SubCategory
    extra = 1
    inlines = [MainSubCategoryInline]

class CatInline(admin.StackedInline):
    model = Category
    extra = 1
    inlines = [SubCatInline]

class StoreNameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['store_name',]}),
    ]
    inlines = [CatInline]
    list_display = ('store_name',)

admin.site.register(StoreName, StoreNameAdmin)

class CatAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['category_name',]}),
    ]
    inlines = [SubCatInline]
    list_display = ('category_name',)
admin.site.register(Category, CatAdmin)

class SubCatAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['sub_category_name',]}),
    ]
    inlines = [MainSubCategoryInline]
    list_display = ('sub_category_name',)
admin.site.register(SubCategory, SubCatAdmin)

