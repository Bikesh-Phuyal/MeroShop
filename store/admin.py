from django.contrib import admin

# Register your models here.

#add an objects into a admin panel
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

