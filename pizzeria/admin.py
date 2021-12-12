from django.contrib import admin
from .models import Pizzeria, Menu, Product
# , Menu, Product, Component, Dupa
# Register your models here.


admin.site.register(Pizzeria)
admin.site.register(Menu)
# admin.site.register(Component)
admin.site.register(Product)
# admin.site.register(Dupa)

