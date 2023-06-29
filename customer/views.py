from django.shortcuts import render, request
from django.view import view


""" Customer will be able to view the landing page"""


class IndexPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, templates/index.html)
