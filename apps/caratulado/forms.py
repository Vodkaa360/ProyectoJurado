from django import forms
from .models import Caratulados

class CaratuladoForm(forms.ModelForm):
    class Meta:
        model = Caratulados
        fields = [
            'nombre', 'nro_expediente', 'provincia', 'tribunal',
            'jurisdiccion', 'evento', 'fecha_inicio', 'fecha_limite', 'completado'
        ]
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_limite': forms.DateInput(attrs={'type': 'date'}),
        }
