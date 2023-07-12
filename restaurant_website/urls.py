"""restaurant_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restaurant.views import IndexPage
from booking.views import ManageBooking


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPage.as_view(), name='index'),
    path('menu_list/', include('menu.urls', namespace='menu_list')),
    path('table_booking/', include('booking.urls', namespace='table_booking')),
    path('manage_booking/', ManageBooking.as_view(), name='manage_booking'),
    path('accounts/', include('allauth.urls')),
]

admin.site.site_header = 'Happy Leeks AdminPanel'
