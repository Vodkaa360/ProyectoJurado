from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from .models import Caratulados

@shared_task
def verificar_fecha_limite_caratulado():
    print("Ejecutando tarea verificar_fecha_limite_caratulado")
    
    umbral_inicio = timezone.now() + timedelta(days=1)
    umbral_fin = timezone.now() + timedelta(days=1, minutes=5)
    
    caratulados_proximos = Caratulados.objects.filter(
        completado=False,
        fecha_limite__gte=umbral_inicio,
        fecha_limite__lt=umbral_fin
    )

    for expediente in caratulados_proximos:
        enviar_alerta_fecha_limite(expediente)

@shared_task
def enviar_recordatorio_fecha_limite():
    print("Ejecutando tarea enviar_recordatorio_fecha_limite")

    hoy = timezone.now().date()
    caratulados_hoy = Caratulados.objects.filter(
        completado=False,
        fecha_limite__date=hoy
    )

    for expediente in caratulados_hoy:
        enviar_alerta_fecha_limite(expediente)

def enviar_alerta_fecha_limite(expediente):
    subject = f"Recordatorio: Hoy es la Fecha Límite para el Expediente {expediente.nro_expediente}"
    message = (
        f"El expediente '{expediente.nombre}' (Número de expediente: {expediente.nro_expediente}) "
        f"tiene la fecha límite el día de hoy ({expediente.fecha_limite.strftime('%d-%m-%Y %H:%M')}). "
    )
    recipient_list = ['vodkaaa360@gmail.com']
    
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
