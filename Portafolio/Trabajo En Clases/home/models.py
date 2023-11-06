from django.db import models

# Create your models here.

class UserPrueba(models.Model):
    first_name = models.CharField(max_length=16, default="Gost User", blank=True, null=True)
    last_name = models.CharField(max_length=16, default="Phantom User")
    age = models.IntegerField(default=1)
    weight = models.FloatField(default=1.5)
    status = models.BooleanField(default=True)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name
