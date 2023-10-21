from django.urls import path
from myapp.samples.pagination_test import views

urlpatterns = [
    path('items/', views.item_list, name='item_list'),
]