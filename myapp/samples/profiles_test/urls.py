from django.urls import path
from myapp.samples.profiles_test import views

urlpatterns = [
    path('create/', views.create_profile, name='create_profile'),
    path('created/', views.profile_created, name='profile_created'),
]