# apps/caratulado/utils/utils.py
import logging
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from apps.caratulado.models import Caratulados

@shared_task
def verificar_fecha_limite_caratulado():
    # Agrega el mensaje de logging
    logging.info("Ejecutando tarea verificar_fecha_limite_caratulado")
    
    umbral_fecha = timezone.now() + timedelta(days=1)
    caratulados_proximos = Caratulados.objects.filter(
        completado=False,
        fecha_limite__lte=umbral_fecha,
        fecha_limite__gt=timezone.now()
    )

    for expediente in caratulados_proximos:
        enviar_alerta_fecha_limite(expediente)

def enviar_alerta_fecha_limite(expediente):
    subject = f"Alerta de Fecha Límite Próxima: Expediente {expediente.nro_expediente}"
    message = (
        f"El expediente '{expediente.nombre}' (Número de expediente: {expediente.nro_expediente}) "
        f"tiene una fecha límite próxima ({expediente.fecha_limite.strftime('%d-%m-%Y %H:%M')}). "
    )
    recipient_list = ['vodkaaa360@gmail.com']
    
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
