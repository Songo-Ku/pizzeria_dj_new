from django.db import models


class Pizzeria(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    phoneNumber = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}'


class Component(models.Model):
    WEIGHT = (
        ('kg', 'kilograms'),
        ('dg', 'dekagrams'),
        ('g', 'grams'),
        ('t', 'tons'),
        ('l', 'litr'),
        ('ml', 'ml'),
        ('m3', 'metr3'),
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    weight = models.CharField(max_length=100, choices=WEIGHT)
    supplier = models.CharField(max_length=100)

    def __str__(self):
        return f'component: {self.name}'


class Product(models.Model):
    FOOD_TYPES = (
        ('appetizer', 'appetizer'),
        ('entree', 'entree'),
        ('dessert', 'dessert'),
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=FOOD_TYPES)
    components = models.ForeignKey(Component, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.OneToOneField(
        Pizzeria,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # wydaje mi sie ze tu powinno byc many to many
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f'Menu from {self.restaurant}'


# to jest zle
class Basket(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)


class Payment(models.Model):
    STATUS_PAYMENT = (
        ('not accepted', 'not accepted'),
        ('accepted', 'accepted'),
    )
    status = models.CharField(max_length=100, choices=STATUS_PAYMENT, default='not accepted')

    def __str__(self):
        return f'{self.status}'

    def get_payment_confirm(self):
        self.status = 'accepted'
        self.save()


class Order(models.Model):
    products = models.ManyToManyField(Product)  # jak tutaj dodawac produkty z Menu.products?
    payment_status = models.OneToOneField(Payment, on_delete=models.CASCADE)  # czy tu moglbybyc foreign key ?

    def __str__(self):
        return f'zamowienie o nr {self.pk} i statusie {self.payment_status}'


# tu powinny znalexc sie produkty z koszyka albo z menu  ???
class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # dlaczego tutaj nie moze byc ManyToManyField
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    # co to znaczy ta meta?
    # class Meta:
    #     constraints = [
    #         models.UniqueField(fields=['pizza', 'order'], name='unique_product_cart')
    #     ]

    def __str__(self):
        return f'zamowiony product to {self.product} w ilosc {self.amount}'












































# class Pictures(models.Model):
#     filename = models.CharField(max_length=50)
#
#     def __str__(self):
#         return f'{self.filename}'
#
#
# class Products(models.Model):
#     name = models.CharField(max_length=128)
#     pictures = models.ManyToManyField(
#         Pictures,
#         through='ProductsPictures',
#     )
#
#     def __str__(self):
#         return f'{self.name}'
#
# class ProductsPictures(models.Model):
#     product = models.ForeignKey(Products, on_delete=models.CASCADE)
#     picture = models.ForeignKey(Pictures, on_delete=models.CASCADE)
#     description = models.CharField(max_length=128)
#
#     def __str__(self):
#         return f'produkt: {self.product} ze zdjeciem {self.picture}'


