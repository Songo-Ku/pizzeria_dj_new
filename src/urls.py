"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from snippets import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pizzeria.urls')),
    path('order-delivery/', include('order_system.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # nie wiem po co to, na pewno nie dziala
    path('api/', include('snippets.urls')),
    path('router/', include(router.urls)),
    # path('api/order_system/', include('api.urls', namespace='api_pizzeria')),  # pytanie czy api powinno byc osobna aplikacja czy znajodwac sie w apkach
]
