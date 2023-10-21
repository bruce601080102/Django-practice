from django.urls import path
from myapp.samples.generic_test import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),  # 瀏覽全部
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # 瀏覽單一資料
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),  # 創建單一資料
]