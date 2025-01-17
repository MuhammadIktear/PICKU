# views.py
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Species, Breed, Color, Size, Sex, Status
from .serializers import SpeciesSerializer, BreedSerializer, ColorSerializer, SizeSerializer, SexSerializer, StatusSerializer

class SpeciesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

class BreedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class ColorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class SizeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class SexViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer

class StatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


