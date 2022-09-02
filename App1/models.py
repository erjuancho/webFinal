from django.db import models

# Create your models here.


class Lacteos(models.Model):
    codigo=models.IntegerField()
    marca=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    precio=models.IntegerField()

    def __str__(self):
        return str(self.codigo)+" "+self.marca+" "+self.tipo

class Galletitas(models.Model):
    codigo=models.IntegerField()
    marca=models.CharField(max_length=50)
    sabor=models.CharField(max_length=50)
    precio=models.IntegerField()

    def __str__(self):
        return str(self.codigo)+" "+self.marca+" "+self.sabor


class Bebidas(models.Model):
    codigo=models.IntegerField()
    marca=models.CharField(max_length=50)
    sabor=models.CharField(max_length=50)
    precio=models.IntegerField()

    def __str__(self):
        return str(self.codigo)+" "+self.marca+" "+self.sabor
