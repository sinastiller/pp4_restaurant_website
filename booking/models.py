from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Booking(models.Model):
    """
    Creates model for table bookings
    """
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    number_of_guests = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(4)])
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name
