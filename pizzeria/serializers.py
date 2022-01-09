from .models import PizzeriaLocal, Pizza, Topping
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class PizzeriaRestaurantSerializer(serializers.ModelSerializer):
    pizzas = serializers.PrimaryKeyRelatedField(many=True, queryset=Pizza.objects.all(), )

    class Meta:
        model = PizzeriaLocal
        fields = ['pk', 'name', 'address', 'phone_number', 'pizzas']


class PizzaSerializer(serializers.ModelSerializer):
    # local = serializers.PrimaryKeyRelatedField()
    # local = PizzeriaRestaurantSerializer()
    # local = serializers.ReadOnlyField(source='local.pk')  # to na pewno nie jest odpowiednie pole dla tego przypadku
    # tu mozliwe ze trzeba dac po prostu int field
    # owner = serializers.ReadOnlyField(source='owner.username')
    restaurant_name = serializers.ReadOnlyField(source='local.name')


    class Meta:
        model = Pizza
        fields = ['pk', 'name', 'price', 'description', 'local', 'restaurant_name']














































# class PizzeriaRestaurantSerializer(serializers.HyperlinkedModelSerializer):
#     pizzas = serializers.PrimaryKeyRelatedField(many=True, queryset=Pizza.objects.all())
#
#     class Meta:
#         model = PizzeriaLocal
#         fields = ['name', 'address', 'phone_number', 'pizzas']


# class PizzaSerializer(serializers.HyperlinkedModelSerializer):
#     # local = serializers.PrimaryKeyRelatedField(read_only=True)
#     # local = PizzeriaRestaurantSerializer()
#     local = serializers.ReadOnlyField(source='local.pk')  # to na pewno nie jest odpowiednie pole dla tego przypadku
#     # tu mozliwe ze trzeba dac po prostu int field
#     # owner = serializers.ReadOnlyField(source='owner.username')
#
#     class Meta:
#         model = Pizza
#         fields = ['name', 'price', 'description', 'local']



