from django.contrib import admin
from .models import *

class Reg_Product(admin.ModelAdmin):
    list_display = ['title', 'short_details', 'price']

admin.site.register(Product, Reg_Product)