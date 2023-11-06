from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return render(request, "home/index.html", {})

# User CRUD
def user_list(request):
    users = user.objects.all()
    return render(request, 'home/user_list.html', {'users': users})

def user_detail(request, pk):
    users = get_object_or_404(user, pk=pk)
    return render(request, 'home/user_detail.html', {'users': users})

def user_new(request):
    if request.method == "POST":
        form = userForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('home/user_detail.html', pk=user.pk)
    else:
        form = userForm()
    return render(request, 'home/user_edit.html', {'form': form})

def user_edit(request, pk):
    user_instance = get_object_or_404(user, pk=pk)
    if request.method == "POST":
        form = userForm(request.POST, request.FILES, instance=user_instance)
        if form.is_valid():
            user_instance = form.save(commit=False)
            user_instance.save()
            return redirect('home/user_detail.html', pk=user.pk)
    else:
        form = userForm(instance=user_instance)
    return render(request, 'home/user_edit.html', {'form': form})

def user_delete(request, pk):
    user_instance = get_object_or_404(user, pk=pk)
    user_instance.delete()
    return redirect('home/user_list.html', pk=user.pk)

#Category CRUDS
# Vista para listar todas las categorías
def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'home/categoria_list.html', {'categorias': categorias})

# Vista para mostrar detalles de una categoría específica
def categoria_detail(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'home/categoria_detail.html', {'categoria': categoria})

# Vista para crear una nueva categoría
def categoria_new(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.save()
            return redirect('categoria_detail', pk=categoria.pk)
    else:
        form = CategoriaForm()
    return render(request, 'home/categoria_edit.html', {'form': form})

# Vista para editar una categoría existente
def categoria_edit(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.save()
            return redirect('categoria_detail', pk=categoria.pk)
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'home/categoria_edit.html', {'form': form})

# Vista para eliminar una categoría
def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    categoria.delete()
    return redirect('categoria_list')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Subcategoria
from .forms import SubcategoriaForm

def subcategoria_list(request):
    subcategorias = Subcategoria.objects.all()
    return render(request, 'home/subcategoria_list.html', {'subcategorias': subcategorias})

def subcategoria_detail(request, pk):
    subcategoria = get_object_or_404(Subcategoria, pk=pk)
    return render(request, 'home/subcategoria_detail.html', {'subcategoria': subcategoria})

def subcategoria_new(request):
    if request.method == "POST":
        form = SubcategoriaForm(request.POST)
        if form.is_valid():
            subcategoria = form.save(commit=False)
            subcategoria.save()
            return redirect('subcategoria_detail', pk=subcategoria.pk)
    else:
        form = SubcategoriaForm()
    return render(request, 'home/subcategoria_edit.html', {'form': form})

def subcategoria_edit(request, pk):
    subcategoria = get_object_or_404(Subcategoria, pk=pk)
    if request.method == "POST":
        form = SubcategoriaForm(request.POST, instance=subcategoria)
        if form.is_valid():
            subcategoria = form.save(commit=False)
            subcategoria.save()
            return redirect('subcategoria_detail', pk=subcategoria.pk)
    else:
        form = SubcategoriaForm(instance=subcategoria)
    return render(request, 'home/subcategoria_edit.html', {'form': form})

def subcategoria_delete(request, pk):
    subcategoria = get_object_or_404(Subcategoria, pk=pk)
    subcategoria.delete()
    return redirect('subcategoria_list')
