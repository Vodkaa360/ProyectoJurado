from django.contrib import admin
from django import forms
from .models import Caratulados

class CaratuladosForm(forms.ModelForm):
    class Meta:
        model = Caratulados
        fields = '__all__'

    class Media:
        js = ('admin/js/caratulados_condicional.js',) 

@admin.register(Caratulados)
class CaratuladosAdmin(admin.ModelAdmin):
    form = CaratuladosForm
    list_display = ('fecha_inicio', 'fecha_limite', 'nombre', 'nro_expediente', 'provincia','tribunal', 'jurisdiccion', 'evento', 'completado')

    list_filter = ('nro_expediente', 'provincia', 'completado', 'evento')
    list_editable = ('completado',)
