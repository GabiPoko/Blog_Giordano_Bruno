from django import forms
from .models import Eventos

class EventoForm (forms.ModelForm):
    model = Eventos
    fields = ['titulo', 'descripcion', 'fecha', 'ubicacion']

    widgets = {
        'fecha': forms.DateInput(attrs={'type':'date'}),
    } 

    
