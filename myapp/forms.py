from django import forms
from myapp.models import Book


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']