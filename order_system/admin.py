from django.contrib import admin
from .models import Order, OrderedPizza, Payment

admin.site.register(Order)
admin.site.register(OrderedPizza)
admin.site.register(Payment)
