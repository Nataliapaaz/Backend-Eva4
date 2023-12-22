from django.db import models

# Create your models here.

class Alumno(models.Model):
    RUT = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    fechaDeNacimiento = models.DateField()
    Email = models.EmailField()

    def __str__(self):
        return f"ID: {self.id} Nombre: {self.nombre} {self.apellido}"

    class Meta:
        db_table = 'alumnos'
