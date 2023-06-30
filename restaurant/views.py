from django.shortcuts import render
from django.views import View
from .models import Menu, Category


class ViewMenu(View):
    """
    View menu items and categories
    """

    def get(self, request, *args, **kwargs):
        colds = Menu.objects.filter(category__name__contains="Chill 'n Thrill")
        hots = Menu.objects.filter(
            category__name__contains='Savoury Temptations')
        sweets = Menu.objects.filter(
            category__name__contains='Sweet Tooth Hugs')
        drinks = Menu.objects.filter(
            category__name__contains='Liquid Delights')

        context = {
            'colds': colds,
            'hots': hots,
            'sweets': sweets,
            'drink': drinks,
        }

        return render(request, '../templates/menu.html', context)
