from django.db import models

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=22, default="AnomUser")
    age = models.IntegerField(default= 18)
    status = models.BooleanField(default=True)
    description = models.CharField(max_length=256, blank=True)
    email = models.CharField(max_length=50, blank=False)
    pfp= models.ImageField(upload_to="profilepictures", blank=True, null=True)

    def __str__(self):
        return self.username

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Subcategoria(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Fabricante(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.producto.nombre} - {self.cantidad} unidades - {self.fecha}'
