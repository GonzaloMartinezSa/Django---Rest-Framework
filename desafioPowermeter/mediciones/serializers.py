from rest_framework import serializers
from .models import Medicion

class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = ['id', 'medicion']
        read_only_fields = ('created_at',)