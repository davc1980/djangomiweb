from django.db import models


# Create your models here.
class Tabla(models.Model):
    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nombre + '-->'+self.genero
