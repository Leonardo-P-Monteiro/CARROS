from django.contrib import admin
from .models import Car, Brand

# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = 'name',
    search_fields = 'name',

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = 'model', 'brand', 'factory_year', 'model_year', 'value',
    search_fields = ('model', 'brand')
