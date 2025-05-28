from django.db import models

# Create your models here.



class Brand(models.Model):
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT,
                              related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/%Y/%m/', blank=True, null=True) #TODO: Precisa ser feito a lógica de redução da qualidade da imagem e padronização do tamanho dela. Isso se faz nos forms antes de salvar. 

    def __str__(self):
        return self.model

class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Count Cars: {self.cars_count} - Total Value: {self.cars_value} - \
            Date: {self.created_at}'
