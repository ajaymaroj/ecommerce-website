from django.contrib import admin
from .models import Customar,Product, Order, OrderItem, ShippingAddresss

# Register your models here.

admin.site.register(Customar)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddresss)