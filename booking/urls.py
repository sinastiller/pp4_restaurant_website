from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.table_booking, name='table_booking'),
]
