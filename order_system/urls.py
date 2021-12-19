from django.urls import path, include

from . import views

app_name = 'order_system'
urlpatterns = [

    path('order-successed', views.OrderSuccessView.as_view(), name='order-successed'),
    path('', views.IndexOrderView.as_view(), name='index'),
    path('order-create/', views.CreateOrderView.as_view(), name='order-create'),
    path('order/<int:id>', views.OrderDetailView.as_view(), name='order-detail'),


    # path('', views.IndexLocalsView.as_view(), name='index'),
    # path('restaurant/<int:id>/', views.LocalDetailView.as_view(), name='index'),
    # path('books_import/', views.BookImportView.as_view(), name='books_import'),
    # path('book/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    # path('add_new_book/', views.BookCreateView.as_view(), name='book_add'),
    # path('<int:id>/delete-book/', views.BookDeleteView.as_view(), name='book_delete'),
    # path('<int:id>/update-book/', views.BookUpdateView.as_view(), name='book_update'),
    # path('booksearchpag/', views.BookListViewSearchView.as_view(), name='booksearchpag'),



]