from django.contrib import admin

# Register your models here.
from formularioProfesor.models import Profesor

# Register your models here.
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['RUT' ,'nombre', 'apellido', 'Telefono', 'Area', 'Email']

admin.site.register(Profesor, ProfesorAdmin)