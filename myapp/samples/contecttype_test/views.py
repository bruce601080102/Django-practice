from django.shortcuts import render
from myapp.samples.contecttype_test.models import ContentBook, ContentReview


def book_detail(request, book_id):
    book = ContentBook.objects.get(pk=book_id)
    reviews = ContentReview.objects.filter(content_type__model='contentbook', object_id=book_id)
    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews})
