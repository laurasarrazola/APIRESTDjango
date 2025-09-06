from django.db import models

# Create your models here.
from django.db import models

#modelo  para las categorías de productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=100) #campo de texto, máximo 100 cacracteres
    descripcion = models.TextField(blank=True) #texto largo opcional

    def __str__(self):
        #devuelve el nombre de la categoría
        return self.nombre

#Modelo para marcas
class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre

#modelo para los productos
class Producto(models.Model):
    nombre = models.CharField(max_length=100) #nombre del producto  
    descripcion = models.TextField(blank=True) #descripción del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE,
        related_name='productos'
    )
    marca = models.ForeignKey(
        Marca,
        on_delete=models.CASCADE,
        related_name='productos',
        default=1
    )
def __str__(self):
    def __str__(self):
        return f"{self.nombre} - {self.precio}"



