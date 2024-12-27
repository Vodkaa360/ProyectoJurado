from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages
from .models import Caratulados
from .forms import CaratuladoForm

class CaratuladoCreateView(CreateView):
    model = Caratulados
    form_class = CaratuladoForm
    template_name = 'caratulado/crear_caratulado.html'
    success_url = reverse_lazy('crear_caratulado')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Caratulado registrado exitosamente.")

        return super().form_valid(form)
