from django.shortcuts import render
from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Usuario
from ..posts.models import Post, Comentario

# Create your views here.

class RegistrarUsuario (CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Registro exitoso.Por favor, inicia sesión.')
        group = Group.objects.get(name='Registrado')
        self.object.groups.add(group)

        return redirect('apps.usuario:registrar')
    
class LoginUsuario (LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login exitoso')

        return reverse ('apps.usuario:login')
    
    
class LogoutUsuario (LogoutView):
    template_name = 'registration/logout.html'

    def get_succes_url (self):
        messages.success(self.request, 'Logout exitoso')

        return reverse('apps.usuario:logout')
    

