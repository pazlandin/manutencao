from rest_framework import serializers
from .models import Escada

class EscadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escada
        fields = '__all__'