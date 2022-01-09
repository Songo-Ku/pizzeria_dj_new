from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from . import viewsets
# app_name = 'pizzeria'

urlpatterns = format_suffix_patterns([
    path('', viewsets.api_root),
    path('pizzeria-restaurants/', viewsets.PizzeriaRestaurantList.as_view(), name='pizzeria-restaurant-list'),
    path('pizzeria-restaurants/<int:pk>/', viewsets.PizzeriaRestaurantDetail.as_view(), name='pizzeria-pizza-detail'),
    path('pizza-create-list/', viewsets.PizzaList.as_view(), name='pizza-create-list'),
    path('pizza-create-list/<int:pk>/', viewsets.PizzaDetail.as_view(), name='pizza-detail-up-del'),
])






# urlpatterns = [
#     path('', views.IndexRestaurantsView.as_view(), name='index'),
#     path('restaurant/add-new/', views.CreateRestaurantView.as_view(), name='restaurant-create'),
#     path('restaurant/<int:id>/', views.RestaurantDetailView.as_view(), name='restaurant-detail'),
#     path('restaurant/menu/<int:id>/', views.MenuRestaurantDetailView.as_view(), name='restaurant-menu'),
# ]