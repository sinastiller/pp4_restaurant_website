from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Table booking form
    """

    class Meta:
        model = Booking
        fields = '__all__'
