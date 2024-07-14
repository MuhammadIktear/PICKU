# serializers.py
from rest_framework import serializers
from pet.models import Pet
from .models import Species, Breed, Color, Size, Sex, Status

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ['id', 'name']

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name']

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name']

class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sex
        fields = ['id', 'name']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name']

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'color', 'size', 'sex', 'image', 'rehoming_fee', 'details', 'status']

    def create(self, validated_data):
        request = self.context.get('request')
        pet = Pet.objects.create(**validated_data, created_by=request.user)
        return pet
