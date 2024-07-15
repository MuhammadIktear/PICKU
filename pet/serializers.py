from rest_framework import serializers
from .models import Adopt, Review, Pet
from filter.serializers import SpeciesSerializer, BreedSerializer, ColorSerializer, SizeSerializer, SexSerializer, StatusSerializer
from filter.models import Species,Sex,Size,Status,Color,Breed

class AdoptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adopt
        fields = ['id', 'user', 'pet', 'adopt_date']
        read_only_fields = ['adopt_date']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'pet', 'user', 'name', 'email', 'body', 'created_on']
        read_only_fields = ['created_on']
    
    def create(self, validated_data):
        review = Review.objects.create(**validated_data)
        return review

class PetSerializer(serializers.ModelSerializer):
    species = SpeciesSerializer()
    breed = BreedSerializer()
    color = ColorSerializer()
    size = SizeSerializer()
    sex = SexSerializer()
    status = StatusSerializer()

    class Meta:
        model = Pet
        fields = '__all__'
    
    def create(self, validated_data):
        # Extract nested serializer data if needed
        species_data = validated_data.pop('species', None)
        breed_data = validated_data.pop('breed', None)
        color_data = validated_data.pop('color', None)
        size_data = validated_data.pop('size', None)
        sex_data = validated_data.pop('sex', None)
        status_data = validated_data.pop('status', None)

        # Create the Pet instance
        request = self.context.get('request')
        pet = Pet.objects.create(created_by=request.user, **validated_data)

        if species_data:
            Species.objects.create(pet=pet, **species_data)
        if breed_data:
            Breed.objects.create(pet=pet, **breed_data)
        if color_data:
            Color.objects.create(pet=pet, **color_data)
        if size_data:
            Size.objects.create(pet=pet, **size_data)
        if sex_data:
            Sex.objects.create(pet=pet, **sex_data)
        if status_data:
            Status.objects.create(pet=pet, **status_data)

        return pet
