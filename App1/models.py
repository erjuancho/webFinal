from django.db import models

# Create your models here.


class Lacteos(models.Model):
    codigo=models.IntegerField()
    marca=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    precio=models.IntegerField()
    cantidad=models.IntegerField()

    def __str__(self):
        return str(self.codigo)+" "+self.marca+" "+self.tipo+" "+str(self.cantidad)

class Galletitas(models.Model):
    codigo=models.IntegerField()
    marca=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    precio=models.IntegerField()
    cantidad=models.IntegerField()

    def __str__(self):
        return str(self.codigo)+" "+self.marca+" "+self.tipo+" "+str(self.cantidad)


class Bebidas(models.Model):
    codigo=models.IntegerField()
    marca=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    precio=models.IntegerField()
    cantidad=models.IntegerField()

    def __str__(self):
        return str(self.codigo)+" "+self.marca+" "+self.tipo+" "+str(self.cantidad)