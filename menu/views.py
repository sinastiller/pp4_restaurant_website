from django.shortcuts import render
from .models import Menu


def menu_list(request):
    menu_list = Menu.objects.all()

    context = {
        'menu_list': menu_list,
    }

    return render(request, '../templates/menu.html', context)
