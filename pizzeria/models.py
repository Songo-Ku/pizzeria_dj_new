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
    pizzas = models.ManyToManyField('Pizza')

    def __str__(self):
        return f'{self.name}'


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    description = models.CharField(max_length=100)
    local = models.ForeignKey(PizzeriaLocal, on_delete=models.CASCADE, related_name='pizzas',)

    def __str__(self):
        return f'name {self.name}, local: {self.local.pk}'







