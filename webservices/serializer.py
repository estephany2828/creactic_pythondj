from rest_framework import serializers
from home.models import *

class producto_serializer (serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('url', 'nombre', 'status', 'foto', 'precio', 'stock', 'marca',)
class marca_serializer (serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('url', 'id', 'nombre',)
class categoria_serializer (serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('url', 'id', 'nombre', )                