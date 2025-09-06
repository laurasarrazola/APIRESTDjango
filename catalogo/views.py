from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response  # Permite devolver respuestas JSON
from rest_framework.decorators import api_view  # Decorador para vistas basadas en función
from .models import Categoria, Producto, Marca
from .serializers import CategoriaSerializer, ProductoSerializer, MarcaSerializer

# Endpoint para listar categorías
@api_view(["GET"])  # Solo permitimos el método GET
def lista_categorias(request):
    categorias = Categoria.objects.all()  # Obtenemos todas las categorías
    serializer = CategoriaSerializer(categorias, many=True)  # Convertimos queryset a JSON
    return Response(serializer.data)  # Devolvemos la lista como JSON

# Endpoint para listar productos
@api_view(["GET"])
def lista_productos(request):
    productos = Producto.objects.all()  # Obtenemos todos los productos
    serializer = ProductoSerializer(productos, many=True)  # Convertimos queryset a JSON
    return Response(serializer.data)  # Devolvemos la lista como JSON

# Endpoint para listar marcas
@api_view(["GET"])
def lista_marcas(request):
    marcas = Marca.objects.all()  # Obtenemos todas las marcas
    serializer = MarcaSerializer(marcas, many=True)  # Convertimos queryset a JSON
    return Response(serializer.data)  # Devolvemos la lista como JSON
