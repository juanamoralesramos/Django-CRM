from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'pais', 'ciudad', 'numero', 'correo']