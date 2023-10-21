from django.urls import path
from  myapp.samples.contecttype_test import views


urlpatterns = [
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]