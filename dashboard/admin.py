from itertools import product
from django import views
from django.contrib import admin
from .models import Product,order
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header= 'Vibe Fm Dashboard'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','quantity','category')
    list_filter=["category"]

admin.site.register(Product, ProductAdmin)
admin.site.register(order)

