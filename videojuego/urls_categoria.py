from django.urls import path
from . import views


app_name = 'categoria'

urlpatterns = [
    path('lista/', views.lista_categoria, name='lista'),
    path('eliminar/<int:id>', views.eliminar_categoria, name='eliminar'),
    path('nuevo/', views.nuevo_categoria, name='nuevo'),

]
