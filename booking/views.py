from django.shortcuts import render, redirect
from django.views import generic, View
from .forms import BookingForm, ManageBooking
from .models import Booking


class ManageBooking(View):
    """
    Customer will be able to view the landing page
    """

    def get(self, request, *args, **kwargs):
        return render(request, '../templates/manage_booking.html')


def table_booking(request):
    booking_form = BookingForm()

    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
            return redirect('manage_booking')
    else:
        booking_form = BookingForm()

    context = {
        'form': booking_form
    }
    return render(request, '../templates/booking.html', context)


def view_booking(request):

    booking = ManageBooking.objects.get()
    
    context = {
            'form': form
        }

    return render(request, '../templates/manage_booking.html', context)