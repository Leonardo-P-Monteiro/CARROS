from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch.dispatcher import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum
from gemini_ai import client

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value = Sum('value')
    )['total_value']

    CarInventory.objects.create(
        cars_count = cars_count,
        cars_value = cars_value,
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = client.get_car_ai_bio(
            brand= instance.brand,
            model= instance.model,
            year= instance.model_year
            )

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()