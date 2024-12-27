from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta


#CHOICES
class Caratulados(models.Model):
    PROVINCIA_CHOICES = [
        ('caba', 'C.A.B.A'),
        ('provincia', 'Provincia de Buenos Aires'),
    ]
    
    EVENTO_CHOICES = [
        ('acompañar estudios', 'Acompañar estudios'),
        ('denuncia fecha de turno', 'Denuncia fecha de turno'),
        ('acompañar documentacion', 'Acompañar documentacion'),
        ('intimacion de pago', 'Intimacion de pago'),
        ('sentencia interlocutoria', 'Sentencia interlocutoria'),
    ]
    
    TRIBUNAL_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]
#GENERAL
    nombre = models.CharField(max_length=100)
    nro_expediente = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_limite = models.DateTimeField(blank=True, null=True)
    evento = models.CharField(max_length=25, choices=EVENTO_CHOICES, null=True)
    completado = models.BooleanField(default=False)
    provincia = models.CharField(max_length=10, choices=PROVINCIA_CHOICES, blank=True, null=True)
    tribunal = models.CharField(max_length=2, choices=TRIBUNAL_CHOICES, null=True, blank=True)
    jurisdiccion = models.CharField(max_length=100, blank=True, null=True)

    # VALIDACIÓN DE FECHAS
    def clean(self):
        super().clean()
        
        # Validación de que `fecha_inicio` y `fecha_limite` caen en días hábiles (Lunes a Viernes)
        if self.fecha_inicio and self.fecha_inicio.weekday() > 4:
            raise ValidationError("La fecha de inicio debe caer en un día hábil (Lunes a Viernes).")
        if self.fecha_limite and self.fecha_limite.weekday() > 4:
            raise ValidationError("La fecha límite debe caer en un día hábil (Lunes a Viernes).")
        if self.fecha_inicio and self.fecha_limite and self.fecha_limite <= self.fecha_inicio:
            raise ValidationError("La fecha límite debe ser posterior a la fecha de inicio.")
        
    def verificar_proximidad_fecha_limite(self):

        if self.fecha_limite:
            return timezone.now() >= (self.fecha_limite - timedelta(days=1)) and not self.completado
        return False

    def __str__(self):
        return f"{self.nombre} - Expediente: {self.nro_expediente} - Límite: {self.fecha_limite}"
