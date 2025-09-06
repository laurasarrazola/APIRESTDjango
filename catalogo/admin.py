from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categoria, Producto, Marca

#Registro basico en el admin
admin.site.register(Categoria) #permite gestionar categorías desde el admin
admin.site.register(Producto) #permite gestionar productos desde el admin
admin.site.register(Marca) #permite gestionar marcas desde el admin
