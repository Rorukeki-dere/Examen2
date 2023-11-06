"""nxtweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index_views"),
    path('user', views.user_list, name='user_list'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
    path('user/new/', views.user_new, name='user_new'),
    path('user/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('user/<int:pk>/delete/', views.user_delete, name='user_delete'),
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('categorias/<int:pk>/', views.categoria_detail, name='categoria_detail'),
    path('categorias/nueva/', views.categoria_new, name='categoria_new'),
    path('categorias/<int:pk>/editar/', views.categoria_edit, name='categoria_edit'),
    path('categorias/<int:pk>/eliminar/', views.categoria_delete, name='categoria_delete'),
    path('subcategorias/', views.subcategoria_list, name='subcategoria_list'),
    path('subcategorias/<int:pk>/', views.subcategoria_detail, name='subcategoria_detail'),
    path('subcategorias/nueva/', views.subcategoria_new, name='subcategoria_new'),
    path('subcategorias/<int:pk>/editar/', views.subcategoria_edit, name='subcategoria_edit'),
    path('subcategorias/<int:pk>/eliminar/', views.subcategoria_delete, name='subcategoria_delete'),
]
