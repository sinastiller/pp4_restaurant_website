from django.shortcuts import render
from django.views import View
# from restaurant.models import Menu


# class IndexPage(View):
#     """
#     Customer will be able to view the landing page
#     """
#     def get(self, request, *args, **kwargs):
#         return render(request, '../templates/index.html')


# class MenuPage(View):
#     def get(self, request, *args, **kwargs):
#         menu_items = Menu.objects.all()

#         context = {
#             'menu_items': menu_items
#         }

#         return render(request, '../templates/menu.html', context)
