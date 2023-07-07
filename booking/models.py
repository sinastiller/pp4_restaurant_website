from django.db import models


class Booking(models.Model):
    """
    Creates model for table bookings
    """
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    number_of_guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name
