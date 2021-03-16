from django.urls import path
from . import views


app_name = 'usuarios'

urlpatterns = [
    # path('lista/', views.lista_categoria, name='lista'),
    # path('eliminar/<int:id>', views.eliminar_categoria, name='eliminar'),
    # path('editar/<int:id>', views.editar_categoria, name='editar'),
    path('nuevo/', views.NuevoUsuario.as_view(), name='nuevo'),
    path('municipios/<int:id_estado>', views.obtiene_municipios, name='municipios'),

]
