from .models import PizzeriaLocal, Pizza, Topping
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class PizzeriaRestaurantSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = PizzeriaLocal
        fields = ['name', 'address', 'phone_number',]


class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    # local = serializers.PrimaryKeyRelatedField(read_only=True)
    local = PizzeriaRestaurantSerializer()


    class Meta:
        model = Pizza
        fields = ['name', 'price', 'description', 'local',]

