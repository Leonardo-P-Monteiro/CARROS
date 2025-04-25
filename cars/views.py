from django.shortcuts import render
from .models import Car
from .forms import CarModelForm

# Create your views here.
def cars_views(request):
    cars = Car.objects.all()
    search = request.GET.get('search')

    if search:
        cars = cars.filter(model__icontains=search)
    
    return render(request, 'cars.html', {'cars':cars})

def new_car_view(request):
    new_car_form = CarModelForm()

    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        
        if new_car_form.is_valid():
            new_car_form.save()

    else:
        new_car_form = CarModelForm()
        
    return render(request, 'new_car.html', {'new_car_form':new_car_form})