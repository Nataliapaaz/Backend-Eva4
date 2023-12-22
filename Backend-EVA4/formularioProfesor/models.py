from django.db import models

# Create your models here.

class Profesor(models.Model):
    RUT = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    Telefono = models.IntegerField()
    Area = models.CharField(max_length=50)
    Email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'profesores'
