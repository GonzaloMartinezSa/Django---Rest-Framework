from .models import Medicion
from rest_framework import viewsets, permissions
from .serializers import MedicionSerializer
import json

class MedicionViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicionSerializer

class MedicionMaxViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.raw('select max(medicion) from mediciones_medicion')
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicionSerializer