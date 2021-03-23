from django.urls import path
from . import views


app_name = 'usuarios'

urlpatterns = [
    path('lista/', views.ListaUsuario.as_view(), name='lista'),
    # path('eliminar/<int:id>', views.eliminar_categoria, name='eliminar'),
    # path('editar/<int:id>', views.editar_categoria, name='editar'),
    path('nuevo/', views.NuevoUsuario.as_view(), name='nuevo'),
    path('login/', views.LoginUsuario.as_view(), name='login'),
    path('municipios/', views.obtiene_municipios, name='municipios'),

]
