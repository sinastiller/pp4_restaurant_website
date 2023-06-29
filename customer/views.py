from django.shortcuts import render
from django.views import View


""" Customer will be able to view the landing page"""


class IndexPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, '../templates/index.html')
