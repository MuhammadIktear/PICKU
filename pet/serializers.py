from rest_framework import serializers
from .models import Pet, Adopt, Review, UserBankAccount

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'name', 'species', 'breed', 'color', 'size', 'sex', 'image', 'rehoming_fee', 'status', 'details', 'created_at']
        read_only_fields = ['created_at']

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
