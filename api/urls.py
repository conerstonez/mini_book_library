from django.urls import path
from api import views

urlpatterns = [
    path('api/', views.BookApiView.as_view(), name='home'),
    path('api/<str:user_input>/', views.get_books_view, name='book_group'),

    path('api/create/', views.BookCreateView.as_view(), name='create_book'),
    path('api/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('api/<int:id>/delete/', views.BookDetailView.as_view(), name='delete_book'),
    path('api/<int:id>/update/', views.BookUpdateView.as_view(), name='update_book'),

    path('api/authors/', views.AuthorApiView.as_view(), name='authors'),
    path('api/authors/create/', views.AuthorCreateView.as_view(), name='create_author'),
    path('api/authors/<int:id>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('api/authors/<int:id>/delete/', views.AuthorDetailView.as_view(), name='delete_author'),
    path('api/authors/<int:id>/update/', views.AuthorUpdateView.as_view(), name='update_author'),
    path('api/authors/<int:id>/books/', views.get_author_books_view, name='author_book_list'),

]
