from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Message
from myapp.forms import BookModelForm
from myapp.models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from myapp.samples.profiles_test.signals import ProfileForm


def hello(request):
    return HttpResponse("Hello Word")


def view_messages(request):
    messages = Message.objects.all()
    for message in messages:
        print(message)
    return render(request, 'messages.html', {'messages': messages})


def create_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        Message.objects.create(content=content)
        return redirect('view_messages')
    return render(request, 'create_message.html')


# ============= 新增表單ModelForm =============
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookModelForm()
    return render(request, 'template_name.html', {'form': form})


# ============= 新增表單Signals =============

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_created')
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})


def profile_created(request):
    return render(request, 'profile_created.html')



