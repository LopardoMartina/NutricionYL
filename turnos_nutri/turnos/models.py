from django.db import models

# Create your models here.
class Turno(models.Model):
    nombre = models.CharField(max_length=250)
    correo = models.EmailField(max_length=250)
    fecha = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre} - {self.fecha.strftime('%d/%m/%Y %H:%M:%S')}"
    