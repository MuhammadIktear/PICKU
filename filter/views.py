# views.py
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from pet.models import Pet
from .models import Species, Breed, Color, Size, Sex, Status
from .serializers import PetSerializer, SpeciesSerializer, BreedSerializer, ColorSerializer, SizeSerializer, SexSerializer, StatusSerializer

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

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def get_queryset(self):
        queryset = Pet.objects.all()
        species = self.request.query_params.get('species')
        breed = self.request.query_params.get('breed')
        color = self.request.query_params.get('color')
        size = self.request.query_params.get('size')
        sex = self.request.query_params.get('sex')
        status = self.request.query_params.get('status')

        if species:
            queryset = queryset.filter(species=species)
        if breed:
            queryset = queryset.filter(breed=breed)
        if color:
            queryset = queryset.filter(color=color)
        if size:
            queryset = queryset.filter(size=size)
        if sex:
            queryset = queryset.filter(sex=sex)
        if status:
            queryset = queryset.filter(status=status)
        
        return queryset
