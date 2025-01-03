from django.db import models
from django.contrib.auth.models import User, AbstractUser  # Asegúrate de importar AbstractUser
from django.utils import timezone
from django.conf import settings  # Importa settings para usar AUTH_USER_MODEL

# Define primero el modelo Espacio
class Espacio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=50)  # Ejemplo: "Aula", "Sento"
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# Luego define el modelo Reserva, que depende de Espacio
class Reserva(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Usar AUTH_USER_MODEL
    espacio = models.ForeignKey('Espacio', on_delete=models.CASCADE)  # Referencia al modelo Espacio como cadena
    fecha = models.DateTimeField()  # Fecha y hora de la reserva
    creado_en = models.DateTimeField(default=timezone.now)  # Fecha de creación de la reserva

    # Devuelve un texto legible para la reserva, por ejemplo: 'Usuario1 reservó Aula1'
    def __str__(self):
        return f"{self.usuario.username} reservó {self.espacio.nombre} el {self.fecha}"

# Define el modelo de usuario personalizado (si lo tienes)
class UserPerfil(AbstractUser):
    es_sensei = models.BooleanField(default=False)
    es_maestro = models.BooleanField(default=False)
    es_alumno = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ("reservar_todos_los_espacios", "Puede reservar todos los espacios"),
            ("reservar_sento", "Puede reservar el Sento"),
            ("consultar_reservas", "Puede consultar reservas futuras"),
        ]
