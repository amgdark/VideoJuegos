from django.urls import path
from . import views


app_name = 'videojuego'

urlpatterns = [
    path('lista/', views.VideojuegoList.as_view(), name='lista'),
    path('nuevo/', views.VideojuegoCrear.as_view(), name='nuevo'),
    path('eliminar/<int:pk>', views.VideojuegoEliminar.as_view(), name='eliminar'),
    path('editar/<int:pk>', views.VideojuegoActualizar.as_view(), name='editar'),
    path('ver/<int:pk>', views.VideojuegoDetalle.as_view(), name='ver'),

]
