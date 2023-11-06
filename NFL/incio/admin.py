from django.contrib import admin

from .models import Ciudad
from .models import Equipos 
from .models import Estadio



@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(Equipos)  
class EquiposAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ciudad'] 

@admin.register(Estadio)
class EstadioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ciudad', 'equipo']