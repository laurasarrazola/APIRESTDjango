from rest_framework import serializers  # Importamos la clase base de serializers
from .models import Categoria, Producto, Marca  # Importamos los modelos que vamos a serializar

# Serializer para la categoría
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria             # Modelo asociado
        fields = ["id", "nombre", "descripcion"]  # Campos que vamos a devolver en JSON

# Serializer para el producto
class ProductoSerializer(serializers.ModelSerializer):
    # Mostramos la categoría como nombre en lugar de solo el ID
    categoria = serializers.StringRelatedField()
    class Meta:
        model = Producto
        fields = ["id", "nombre", "descripcion", "precio", "categoria"]

# Serializer para marca
class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ["id", "nombre", "pais"]