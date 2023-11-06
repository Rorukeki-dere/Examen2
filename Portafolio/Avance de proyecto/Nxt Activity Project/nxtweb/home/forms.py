from django import forms
from .models import *

class userForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['username', 'age', 'status', 'description', 'email', 'pfp']
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class SubcategoriaForm(forms.ModelForm):
    class Meta:
        model = Subcategoria
        fields = ['nombre', 'categoria']