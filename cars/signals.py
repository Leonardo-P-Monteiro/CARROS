from django.db.models.signals import pre_save, pre_delete, post_save, \
post_delete
from django.dispatch.dispatcher import receiver
from cars.models import Car

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    car_model = instance.model

    print('###### Meu primeiro signal: pré-save ######')
    print(f'O modelo de carro "{car_model}" foi CRIADO e depois SALVO.')
    print(instance)

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_model = instance.model

    print('###### Meu segundo signal: pós-save ######')
    print(f'O modelo de carro "{car_model}" foi SALVO.')
    print(instance)