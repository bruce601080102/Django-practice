from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Message(models.Model):
    content = models.TextField()

    class Meta:
        db_table = 'custom_message2'
        
        
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    # published_date = models.DateField()
    published_date = models.CharField(max_length=100)
    


