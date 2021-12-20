from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views




# app_name = 'snippets'
urlpatterns = [
    # path('', views.IndexRestaurantsView.as_view(), name='index'),
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)