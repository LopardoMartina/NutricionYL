from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Turno(models.Model):
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='turnos', null=True, blank=True)
    fecha = models.DateField()
    hora = models.TimeField(null=True, blank=True)
    tipo_consulta = models.CharField(max_length=250)
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"{self.paciente} - {self.fecha} {self.hora}"


class Paciente(AbstractUser):
    nombre = models.CharField(max_length=250, default='Sin nombre')
    apellido = models.CharField(max_length=250, blank=True, null=True)
    edad = models.IntegerField(default=0)
    dni = models.CharField(max_length=20, unique=True, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return  f"{self.nombre} {self.apellido or ''}".strip()

class HistorialClinico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='historiales')
    fecha = models.DateField()
    hora = models.TimeField()
    tipo_consulta = models.CharField(max_length=250)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.paciente} - {self.fecha} {self.hora}"


class PerfilProfesional(models.Model):
    nombre_completo = models.CharField(max_length=250)
    especialidad = models.CharField(max_length=250)
    email = models.EmailField()
    telefono = models.CharField(max_length=250)
    horario_semana_inicio = models.TimeField()
    horario_semana_fin = models.TimeField()
    horario_sabado_inicio = models.TimeField()
    horario_sabado_fin = models.TimeField()

    def __str__(self):
        return self.nombre_completo