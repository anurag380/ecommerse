from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Contact)
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Orderline)
admin.site.register(Category)
admin.site.register(Tag)