from django.urls import path
from .views import ListarEventosView, DetalleEventoView, CrearEventoView, ActualizarEventoView, EliminarEventoView

app_name= 'apps.eventos' 


urlpatterns = [
    path('', ListarEventosView.as_view(), name='lista_eventos'),
    path('<int:pk>/', DetalleEventoView.as_view(), name='detalle_evento'),
    path('crear/', CrearEventoView.as_view(), name='crear_evento'),
    path('editar/<int:pk>/', ActualizarEventoView.as_view(), name='actualizar_evento'),
    path('eliminar/<int:pk>/', EliminarEventoView.as_view(), name='eliminar_evento'),
]