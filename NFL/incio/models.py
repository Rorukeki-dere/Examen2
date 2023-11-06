from django.db import models


class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
      verbose_name_plural = 'CIUDAD'
    def __str__(self):
        return self.nombre


class Equipos(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = 'EQUIPOS'


class Estadio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipos, on_delete=models.CASCADE)
    class Meta:
            verbose_name_plural = 'ESTADIO'
    def __str__(self):
        return self.nombre