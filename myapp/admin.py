from django.contrib import admin

# Register your models here.
from django.apps import apps

# 获取所有已注册的模型
all_models = apps.get_models()

# 自动注册自定义应用程序中的模型
for model in all_models:
    if model._meta.app_label != 'auth':
        admin.site.register(model)
