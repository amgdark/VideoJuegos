from django.urls import path
from . import views


app_name = 'videojuego'

urlpatterns = [
    path('lista/', views.lista_categoria, name='lista'),
    path('eliminar/<int:id>', views.eliminar_categoria, name='eliminar'),

]
