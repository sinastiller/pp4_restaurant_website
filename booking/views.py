from django.shortcuts import render, redirect, reverse
from django.views import generic, View
from .forms import BookingForm
from .models import Booking


def table_booking(request):
    booking_form = BookingForm()

    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.instance.name = request.user
            booking_form.save()
            return redirect(reverse('booking:manage_booking'))
    else:
        booking_form = BookingForm()

    context = {
        'form': booking_form
    }
    return render(request, '../templates/booking.html', context)


class BookingsList(generic.View):
    """
    Customer will be able to view their booking/s
    """
    model = Booking
    queryset = Booking.objects.all()
    template_name = 'manage_booking.html'
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            bookings = Booking.objects.filter(name=request.user)
            context = {
                'bookings': bookings
            }

            return render(request, 'manage_booking.html', context)
