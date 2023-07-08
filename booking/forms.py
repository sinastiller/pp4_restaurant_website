from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Table booking form
    """

    date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'placeholder': 'dd/mm/yyyy',
        }))

    phone = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'placeholder': '0123456789',
                }
            )
        )

    class Meta:
        model = Booking
        fields = '__all__'
