from django.db import models
from django.utils.text import slugify


class Menu(models.Model):
    """
    Creates the menu model
    """
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'menu item'
        verbose_name_plural = 'menuitems'

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Menu, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
