from django.views.generic import ListView, DetailView, CreateView
from myapp.samples.generic_test.models import BookGeneric
from django.urls import reverse_lazy


class PostListView(ListView):
    model = BookGeneric
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = BookGeneric
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = BookGeneric
    template_name = 'post_form.html'
    fields = ['title', 'author', 'publication_date']
    success_url = reverse_lazy('post_list')
    
    
# # 自定义列表视图
"""
# 不使用視圖的方式
from django.shortcuts import render, redirect
class PostListView(View):
    def get(self, request):
        books = BookGeneric.objects.all()
        return render(request, 'post_list.html', {'posts': books})

class PostDetailView(View):
    def get(self, request, pk):
        book = BookGeneric.objects.get(pk=pk)
        return render(request, 'post_detail.html', {'post': book})

class PostCreateView(View):
    def get(self, request):
        form = BookGenericForm()
        return render(request, 'post_form.html', {'form': form})

    def post(self, request):
        form = BookGenericForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('post_list')  
        return render(request, 'post_form.html', {'form': form})

"""


