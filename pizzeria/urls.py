from django.urls import path, include

from . import views

app_name = 'pizzeria'
urlpatterns = [
    path('', views.IndexRestaurantsView.as_view(), name='index'),
    path('restaurant/add-new/', views.CreateRestaurantView.as_view(), name='restaurant-create'),
    path('restaurant/<int:id>/', views.RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('restaurant/menu/<int:id>/', views.MenuRestaurantDetailView.as_view(), name='restaurant-menu'),




    # path('books_import/', views.BookImportView.as_view(), name='books_import'),
    # path('book/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    # path('add_new_book/', views.BookCreateView.as_view(), name='book_add'),
    # path('<int:id>/delete-book/', views.BookDeleteView.as_view(), name='book_delete'),
    # path('<int:id>/update-book/', views.BookUpdateView.as_view(), name='book_update'),
    # path('booksearchpag/', views.BookListViewSearchView.as_view(), name='booksearchpag'),



]