from django.forms import ModelForm
from .models import Ciudad, Equipos, Estadio


class CrearFormularioCiudad(ModelForm):
    class Meta:
        model=Ciudad
        fields=['name']

class CrearFormularioEquipo(ModelForm):
    class Meta:
        model=Equipos
        fields=['name']

class CrearFormularioEstadio(ModelForm):
    class Meta:
        model=Estadio
    
        fields=['name']