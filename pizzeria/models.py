from django.db import models


FOOD_TYPES = (
    ('appetizer', 'appetizer'),
    ('entree', 'entree'),
    ('dessert', 'dessert'),
)
WEIGHT = (
    ('kg', 'kilograms'),
    ('dg', 'dekagrams'),
    ('g', 'grams'),
    ('t', 'tons')
)


class Pizzeria(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    phoneNumber = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}'


class Component(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    weight = models.CharField(max_length=100, choices=WEIGHT)
    supplier = models.CharField(max_length=100)

    def __str__(self):
        return f'component: {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=FOOD_TYPES)
    components = models.ManyToManyField(
        Component)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.OneToOneField(
        Pizzeria,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'Menu from {self.restaurant}'


class Payment(models.Model):
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.status}'

    def get_payment_confirm(self):
        self.status = True
        self.save()


# class OrderProduct(models.Model):
#     price = models.DecimalField(),
#     name = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='ordered_product')
#
#
# class Order(models.Model):
#     status = Payment




