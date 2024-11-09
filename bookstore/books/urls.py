from django.urls import path
from .views import BooklistCreate,BookDetail

urlpatterns = [
    path('books/',BooklistCreate.as_view(),name='book-list-create'),
    path('books/<int:pk>/',BookDetail.as_view(),name='book-detail'),
]