from django.contrib import admin
from formularioAlumno.models import Alumno

# Register your models here.
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['RUT' ,'nombre', 'apellido', 'carrera', 'fechaDeNacimiento', 'Email']

admin.site.register(Alumno, AlumnoAdmin)