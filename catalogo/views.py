from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response  # Permite devolver respuestas JSON
from rest_framework.decorators import api_view  # Decorador para vistas basadas en función
from rest_framework import status                
from django.shortcuts import get_object_or_404  
from .models import Categoria, Producto, Marca
from .serializers import CategoriaSerializer, ProductoSerializer, MarcaSerializer





# -------------------------------
# CRUD para Marcas
# -------------------------------
# Endpoint para listar marcas
@api_view(["GET"])  # Solo permitimos el método GET
def lista_marcas(request):
    marcas = Marca.objects.all()  # Obtenemos todas las marcas
    serializer = MarcaSerializer(marcas, many=True)  # Convertimos queryset a JSON
    return Response(serializer.data)  # Devolvemos la lista como JSON

# Endpoint para obtener el detalle de una marca
@api_view(["GET"])
def detalle_marca(request, pk):
    # Buscamos la marca por ID (pk = primary key)
    marca = get_object_or_404(Marca, pk=pk)
    # Serializamos el objeto encontrado
    serializer = MarcaSerializer(marca)
    # Devolvemos el objeto como JSON
    return Response(serializer.data, status=status.HTTP_200_OK)

# Endpoint para crear una nueva marca
@api_view(["POST"])
def crear_marca(request):
    # Creamos un serializador con los datos enviados en la petición
    serializer = MarcaSerializer(data=request.data)
    # Validamos si los datos son correctos
    if serializer.is_valid():
        serializer.save()  # Guardamos en la BD
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # Si hay errores, devolvemos el error en JSON
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Endpoint para actualizar una marca existente
@api_view(["PUT"])
def actualizar_marca(request, pk):
    # Buscamos la marca a actualizar
    marca = get_object_or_404(Marca, pk=pk)
    # Pasamos el objeto y los datos nuevos al serializador
    serializer = MarcaSerializer(marca, data=request.data)
    if serializer.is_valid():
        serializer.save()  # Guardamos cambios
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Endpoint para eliminar una marca
@api_view(["DELETE"])
def eliminar_marca(request, pk):
    # Buscamos la marca
    marca = get_object_or_404(Marca, pk=pk)
    marca.delete()  # Eliminamos
    return Response({"mensaje": "Marca eliminada"}, status=status.HTTP_204_NO_CONTENT)


# -------------------------------
# CRUD para Categorías
# -------------------------------
# Endpoint para listar categorías
@api_view(["GET"])  # Solo permitimos el método GET
def lista_categorias(request):
    categorias = Categoria.objects.all()  # Obtenemos todas las categorías
    serializer = CategoriaSerializer(categorias, many=True)  # Convertimos queryset a JSON
    return Response(serializer.data)  # Devolvemos la lista como JSON

# Endpoint para obtener el detalle de una categoría
@api_view(["GET"])
def detalle_categoria(request, pk):
    # Buscamos la categoría por ID (pk = primary key)
    categoria = get_object_or_404(Categoria, pk=pk)
    # Serializamos el objeto encontrado
    serializer = CategoriaSerializer(categoria)
    # Devolvemos el objeto como JSON
    return Response(serializer.data, status=status.HTTP_200_OK)

# Endpoint para crear una nueva categoría
@api_view(["POST"])
def crear_categoria(request):
    # Creamos un serializador con los datos enviados en la petición
    serializer = CategoriaSerializer(data=request.data)
    # Validamos si los datos son correctos
    if serializer.is_valid():
        serializer.save()  # Guardamos en la BD
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # Si hay errores, devolvemos el error en JSON
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Endpoint para actualizar una categoría existente
@api_view(["PUT"])
def actualizar_categoria(request, pk):
    # Buscamos la categoría a actualizar
    categoria = get_object_or_404(Categoria, pk=pk)
    # Pasamos el objeto y los datos nuevos al serializador
    serializer = CategoriaSerializer(categoria, data=request.data)
    if serializer.is_valid():
        serializer.save()  # Guardamos cambios
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Endpoint para eliminar una categoría
@api_view(["DELETE"])
def eliminar_categoria(request, pk):
    # Buscamos la categoría
    categoria = get_object_or_404(Categoria, pk=pk)
    categoria.delete()  # Eliminamos
    return Response({"mensaje": "Categoría eliminada"}, status=status.HTTP_204_NO_CONTENT)


# -------------------------------
# CRUD para Productos
# -------------------------------
# Endpoint para listar productos
@api_view(["GET"])
def lista_productos(request):
    productos = Producto.objects.all()  # Obtenemos todos los productos
    serializer = ProductoSerializer(productos, many=True)  # Convertimos queryset a JSON
    return Response(serializer.data)  # Devolvemos la lista como JSON

# Endpoint para obtener el detalle de un producto
@api_view(["GET"])
def detalle_producto(request, pk):
    # Buscamos el producto por ID
    producto = get_object_or_404(Producto, pk=pk)
    # Serializamos el producto
    serializer = ProductoSerializer(producto)
    # Devolvemos el producto como JSON
    return Response(serializer.data, status=status.HTTP_200_OK)

# Endpoint para crear un nuevo producto
@api_view(["POST"])
def crear_producto(request):
    serializer = ProductoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Endpoint para actualizar un producto existente
@api_view(["PUT"])
def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    serializer = ProductoSerializer(producto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Endpoint para eliminar un producto
@api_view(["DELETE"])
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return Response({"mensaje": "Producto eliminado"}, status=status.HTTP_204_NO_CONTENT)

