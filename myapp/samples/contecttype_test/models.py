# generic_relation_example/models.py

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db import IntegrityError


class ContentAuthor(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ContentBook(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(ContentAuthor, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.title


# ContentType可以指定關聯哪一個表單
class ContentReview(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    text = models.TextField()

    def __str__(self):
        return f"Review of {self.content_object}"


def save_contect(name, title, text):
    # 創建作者
    author = ContentAuthor.objects.create(name=name)
    # 創建書籍並關聯到作者
    book = ContentBook.objects.create(title=title, author=author)
    # 創建及評論
    review = ContentReview.objects.create(content_type_id=ContentType.objects.get_for_model(ContentBook).id, object_id=book.id, text=text)
    print("Sample data created successfully.")


# save_contect(name="J.K. Rowling", title="Harry Potter and the Sorcerer's Stone", text="Great book!")


