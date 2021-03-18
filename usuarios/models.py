from django.db import models
from django.contrib.auth.models import User


class Usuario(User):
    estado = models.ForeignKey("usuarios.Estado", verbose_name="Estado", on_delete=models.CASCADE)
    municipio = models.ForeignKey("usuarios.Municipio", verbose_name="Municipio", on_delete=models.CASCADE)
    foto = models.ImageField("Foto de perfil", upload_to='perfiles', blank=True, null=True)

class Estado(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Municipio(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.ForeignKey("usuarios.Estado", verbose_name="Estado", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre