from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from .models import Ciudad, Equipos, Estadio
from .forms import CrearFormularioCiudad, CrearFormularioEquipo, CrearFormularioEstadio

def NFLInicio(request):
    ciudades = Ciudad.objects.all()
    equipos = Equipos.objects.all()
    estadios = Estadio.objects.all()
    return render(request, 'Inicio.html', {'ciudades': ciudades, 'equipos': equipos, 'estadios': estadios})

def crear(request):
    if request.method=='GET':
         return render(request,'crear.html',{
        'form': CrearFormularioCiudad
    })
    else:
        try:

            formVar=CrearFormularioCiudad(request.POST)
            formVar.save() 
            return redirect('/')
        except ValueError:
           return render (request,'crear.html', {
        'form': CrearFormularioCiudad,
        'error':'Porfavor envia datos validos'
    })  
        






        

def modificar_ciudad(request, id):
    try:
        identificarciudad = get_object_or_404(Ciudad, id=id)
    except Ciudad.DoesNotExist:
        raise Http404("La ciudad no fue encontrada")  # Levanta una excepción 404 personalizada

    data = {
        'form': CrearFormularioCiudad(instance=identificarciudad)
    }

    if request.method == 'POST':
        formularioNuevo = CrearFormularioCiudad(data=request.POST, instance=identificarciudad)
        if formularioNuevo.is_valid():
            formularioNuevo.save()
            data['mensaje'] = "Modificado correctamente"
            data['form'] = formularioNuevo
            # Redirige a la página de inicio
            return redirect('/')

    return render(request, 'editar.html', data)

def eliminar(request, id):
    eliminaR=get_object_or_404(Ciudad,id=id)
    eliminaR.delete()
    return redirect('/')