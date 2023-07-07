from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('time',)
    search_fields = ['name', 'date']
