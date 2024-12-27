from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Configura el módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JuradoProject.settings')

app = Celery('JuradoProject')

# Carga la configuración de Django con el prefijo `CELERY`
app.config_from_object('django.conf:settings', namespace='CELERY')

# Asegúrate de que `autodiscover_tasks` esté habilitado
app.autodiscover_tasks()
