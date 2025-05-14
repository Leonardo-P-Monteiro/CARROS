from django import forms
from .models import Brand, Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value','')
        if value < 20_000:
            self.add_error('value', 'O valor do carro não pode ser mernor do \
                           que R$ 20.000,00.')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year', '')
        if factory_year < 1975:
            self.add_error('factory_year', 'Veículo muito velho, não pode ser \
                           cadastrado.')
        return factory_year