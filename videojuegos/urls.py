
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias/', include('videojuego.urls_categoria')),
    path('videojuegos/', include('videojuego.urls_videojuego')),
    path('usuarios/', include('usuarios.urls')),
]
