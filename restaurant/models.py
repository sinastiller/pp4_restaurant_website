from django.db import models


class Menu(models.Model):
    """
    Add item to menu as admin
    """
    category = models.ManyToManyField('Category', related_name='item')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name
        return str(self.price) + ": €"


class Category(models.Model):
    """
    Add category to menu item
    """
    name = models.CharField(max_length=50, blank=True)
    slug - models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name
