from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from .forms import BookingForm
from .models import Booking


def table_booking(request):
    """
    Lets user create a booking
    """
    booking_form = BookingForm()

    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.instance.name = request.user
            booking_form.save()
            messages.success(request, 'Booking successful.')
            return redirect(reverse('booking:manage_booking'))
        else:
            messages.error(request, 'Booking unsuccessful. Please try again.')
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
                'bookings': bookings,
            }

            return render(request, 'manage_booking.html', context)


def edit_booking(request, booking_id):
    """
    Lets user updated their booking
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking_form = BookingForm(request.POST, instance=booking)
        if booking_form.is_valid():
            booking_form.save()
            messages.success(request, 'Booking updated successfully.')
            return redirect('booking:manage_booking')
        else:
            messages.error(request, 'Update unsuccessful. Please try again.')

    booking_form = BookingForm(instance=booking)

    return render(request, 'edit_booking.html', {'form': booking_form})


def delete_booking(request, booking_id):
    """
    Lets user delete their booking
    """
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.success(request, 'Booking deleted successfully.')
    return redirect('booking:manage_booking')
