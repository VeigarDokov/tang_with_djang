"""Required modules for admin page"""
from django.contrib import admin
from rango.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    """It will add title category and url to admin web page"""
    list_display = ("title", "category", "url")


class CategoryAdmin(admin.ModelAdmin):
    """It will automatically populate slug field as you type in categry name"""
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
# adjust Django administration to Smart Relay d.o.o in django system file
# visit nex file on vebserver because it is not inclouded in git:
# /venv_tang_wit_djang/lib/python3.11/site-packages/django/contrib/admin/
# templates/admin/base_site.html
