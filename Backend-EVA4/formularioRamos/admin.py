from django.contrib import admin
from formularioRamos.models import Ramos

# Register your models here.
class RamosAdmin(admin.ModelAdmin):
    list_display = ['idRamo' ,'nombre', 'carrera', 'descripcion', 'creditos', 'horas', 'sala']

admin.site.register(Ramos, RamosAdmin)