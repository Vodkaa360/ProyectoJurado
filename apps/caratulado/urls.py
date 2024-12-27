from django.urls import path
from .views import CaratuladoCreateView

urlpatterns = [
    path('crear_caratulado/', CaratuladoCreateView.as_view(), name='crear_caratulado'),
]
