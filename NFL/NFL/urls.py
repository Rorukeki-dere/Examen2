"""
URL configuration for NFL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Inicio import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.NFLInicio),
    path('registrar/', views.Ciudad, name='ciudad_txt'),
     path('crear/', views.crear, name='crear_txt'),
    
     path('editar/<id>/', views.modificar_ciudad, name='modificar_ciudad'), #parametro dinamico al recibir diferentes variables
 path('eliminar/<id>/', views.eliminar, name='eliminar'), #parametro dinamico al recibi
]