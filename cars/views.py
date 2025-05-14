from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from .models import Car
from .forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, \
    DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.


class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
        qs = super().get_queryset().order_by('model')
        search = self.request.GET.get('search', '')

        if search:
            qs = qs.filter(model__icontains=search)

        return qs

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

class NewCarCreateView( LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'
    login_url = 'login'
    redirect_field_name = 'next'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self) -> str:
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk}) #type:ignore

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'
    
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)