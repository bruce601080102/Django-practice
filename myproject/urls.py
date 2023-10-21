"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from .views import hello
from myapp.views import hello
from myapp import views
from django.conf.urls.i18n import i18n_patterns
from django.urls import re_path
from myapp.samples.translation_test import views as trans_views
from myapp.samples.selectdb_test.models import create_entry


urlpatterns = i18n_patterns(
    re_path(r'^multilingual/$', trans_views.home, name='home'),
    path('i18n/', include('django.conf.urls.i18n')),
    prefix_default_language=False,  # 如果你不想在默认语言的URL前加上语言前缀
)
# 不想支援有多語系的就放在這裡
urlpatterns += [
    path('admin/', admin.site.urls),
    path('', hello, name='hello'),
    path('get_messages/', views.view_messages, name='view_messages'),
    path('create_messages/', views.create_message, name='create_message'),
    
    path('form/add/', views.add_book, name='add_book'),
    path('form/books/', views.book_list, name='book_list'),
    
    path('profiles/', include('myapp.samples.profiles_test.urls')),
    
    path('generic/', include('myapp.samples.generic_test.urls')),
    
    path('pagination/', include('myapp.samples.pagination_test.urls')),
    
    path('contecttype/', include('myapp.samples.contecttype_test.urls')),
    
    # path('otherdb/', include('myapp.samples.selectdb_test.urls')),
]

try:
    create_entry()
except Exception:
    print("尚未創建table")
