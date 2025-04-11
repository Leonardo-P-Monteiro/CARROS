from django.contrib import admin
from .models import Car

# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = 'model', 'brand', 'factory_year', 'model_year', 'value',
    search_fields = ('model',)