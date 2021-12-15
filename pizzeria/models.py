from django.db import models


class PizzeriaLocal(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}'


class Topping(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    supplier = models.CharField(max_length=100)

    def __str__(self):
        return f'topping: {self.name}'


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    description = models.CharField(max_length=100)
    topping = models.ManyToManyField('Topping')
    local = models.ForeignKey(PizzeriaLocal, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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
    # czy tu powinno byc takie polaczenie albo foreign key no i czy nie wstawic tego w payment
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)

    def __str__(self):
        return f'zamowienie o nr {self.pk} i statusie {self.payment}'


class OrderedPizza(models.Model):
    pizza_name = models.CharField(max_length=20)  # dlaczego tutaj nie moze byc ManyToManyField
    amount = models.IntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    order = models.ForeignKey(Order, models.CASCADE)

    def __str__(self):
        return f'zamowiona pizza to {self.pizza_name} w ilosc {self.amount} za {self.amount * self.price}'





