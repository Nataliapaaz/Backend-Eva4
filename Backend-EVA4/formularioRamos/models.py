from django.db import models
from formularioAlumno.models import Alumno
from formularioProfesor.models import Profesor

# Create your models here.
class Ramos(models.Model):
    idRamo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    carrera = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=40)
    creditos = models.IntegerField()
    horas = models.IntegerField()
    sala = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'ramos'

class InfoRamo(models.Model):
    ramo = models.ForeignKey(
        Ramos, on_delete=models.CASCADE, related_name='Info')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"InfoRamo {self.ramo.nombre} - Carrera {self.ramo.carrera}, Profesor {self.profesor.nombre}"


    class Meta:
        db_table = 'inforamo'