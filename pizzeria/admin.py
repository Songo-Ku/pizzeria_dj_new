from django.contrib import admin
# from .models import Pizzeria, Menu, Product
# from .models import Pictures, Products, ProductsPictures
from .models import Order, OrderedPizza, PizzeriaLocal, Payment, Pizza, Topping

admin.site.register(Order)
admin.site.register(OrderedPizza)
admin.site.register(PizzeriaLocal)
admin.site.register(Topping)
admin.site.register(Payment)


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'local')

# admin.site.register(Pictures)
# admin.site.register(Products)
# admin.site.register(ProductsPictures)



