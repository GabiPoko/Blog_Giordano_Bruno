from django.urls import path
from . import views

apps_name = 'contacto'

urlpatterns = [
    path ('contacto/', views.ContactoUsuario.as_view(), name = 'contacto'),
]