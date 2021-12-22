from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import mixins, generics
from rest_framework import viewsets, status, permissions

from .serializers import PizzeriaRestaurantSerializer, PizzaSerializer
from .models import PizzeriaLocal, Pizza, Topping


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'restaurants-list': reverse('pizzeria-restaurant-list', request=request, format=format),
        # 'pizzeria-pizza-detail': reverse('pizzeria-pizza-detail', request=request, format=format),
    })


class PizzeriaRestaurantList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = PizzeriaLocal.objects.all()
    serializer_class = PizzeriaRestaurantSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class PizzeriaRestaurantDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = PizzeriaLocal.objects.all()
    serializer_class = PizzeriaRestaurantSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PizzaViewSets(
    generics.ListAPIView,
):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]


class PizzaCreateListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

