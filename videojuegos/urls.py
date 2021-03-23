
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias/', include('videojuego.urls_categoria')),
    path('videojuegos/', include('videojuego.urls_videojuego')),
    path('usuarios/', include('usuarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
