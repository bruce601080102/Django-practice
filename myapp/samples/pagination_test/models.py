from django.db import models
from django.db import IntegrityError


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

def save_pagination(name):
    try:
        pagination = Item(name=name)
        pagination.save()
    except IntegrityError as e:
        print("Caught an integrity error:", e)

try:
    save_pagination("John")
    save_pagination("John1")
    save_pagination("Bruce")
    save_pagination("John2")
    save_pagination("John3")
    save_pagination("John4")
    
except Exception:
    print("尚未創建")