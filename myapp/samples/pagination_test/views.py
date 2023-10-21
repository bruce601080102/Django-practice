from django.shortcuts import render
from django.core.paginator import Paginator
from myapp.samples.pagination_test.models import Item


def item_list(request):
    items = Item.objects.all()
    paginator = Paginator(items, 3)  # 每页显示10个项

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'item_list.html', {'page': page})