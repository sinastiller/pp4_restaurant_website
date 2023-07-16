from django.urls import path
from . import views


app_name = 'booking'

urlpatterns = [
    path('', views.table_booking, name='table_booking'),
    path('manage_booking/',
         views.BookingsList.as_view(), name='manage_booking'),
    path('edit_booking/<booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete_booking/<booking_id>/', views.delete_booking, name='delete_booking')
]
