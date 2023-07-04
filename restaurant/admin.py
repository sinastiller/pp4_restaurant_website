from django.contrib import admin
from .models import Menu
# , Category


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    search_fields = ['name', 'category']
    prepopulated_fields = {'slug': ('name',)}
# admin.site.register(Category)
