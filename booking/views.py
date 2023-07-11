from django.shortcuts import render, redirect
from .forms import BookingForm


def table_booking(request):
    booking_form = BookingForm()

    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
            return redirect('index')
            # return HttpResponseRedirect("/thanks/")
    else:
        booking_form = BookingForm()

    context = {
        'form': booking_form
    }
    return render(request, '../templates/booking.html', context)
