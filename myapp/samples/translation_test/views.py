from django.shortcuts import render
from django.utils.translation import gettext as _


def home(request):
    context = {
        'message': _("Welcome to our website!")
    }
    return render(request, 'home.html', context)
