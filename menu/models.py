from django.db import models


class Menu(models.Model):
    """
    Create the menu model
    """
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
