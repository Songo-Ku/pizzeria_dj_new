from .models import Pizza, PizzeriaLocal, Topping
from .serializers import PizzaSerializer, PizzeriaRestaurantSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework import permissions
from rest_framework import status
from rest_framework import serializers


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'restaurants': reverse('pizzeria-restaurant-list', request=request, format=format),
        'pizzas': reverse('pizza-create-list', request=request, format=format)
    })


class PizzaList(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()





class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PizzeriaRestaurantList(generics.ListCreateAPIView):
    queryset = PizzeriaLocal.objects.all()
    serializer_class = PizzeriaRestaurantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PizzeriaRestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PizzeriaLocal.objects.all()
    serializer_class = PizzeriaRestaurantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

