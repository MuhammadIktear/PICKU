from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from .models import Pet, Adopt, Review
from users.models import UserAccount
from .serializers import PetSerializer, AdoptSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class PetListAPIView(generics.ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [AllowAny]

class PetDetailAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [AllowAny]

class AdoptPetAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, pet_id):
        pet = get_object_or_404(Pet, id=pet_id)
        user = request.user
        bank_account = get_object_or_404(UserAccount, user=user)
        if pet.status != 'Available To Adopt':
            return Response({"error": "This pet is not available for adoption."}, status=status.HTTP_400_BAD_REQUEST)

        if bank_account.balance < pet.rehoming_fee:
            return Response({"error": "Insufficient balance."}, status=status.HTTP_400_BAD_REQUEST)

        bank_account.balance -= pet.rehoming_fee
        Adopt.objects.create(user=request.user, pet=pet)
        bank_account.save()

        adoption = Adopt.objects.create(user=user, pet=pet)
        serializer = AdoptSerializer(adoption)
        pet.status = 'Adopted'
        pet.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class PetUpdateAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get_object(self, pet_id, user):
        try:
            pet = Pet.objects.get(id=pet_id, created_by=user)
            return pet
        except Pet.DoesNotExist:
            return None

    def put(self, request, pet_id):
        pet = self.get_object(pet_id, request.user)
        if not pet:
            return Response({"error": "You do not have permission to update this pet or it does not exist."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = PetSerializer(pet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pet_id):
        pet = self.get_object(pet_id, request.user)
        if not pet:
            return Response({"error": "You do not have permission to delete this pet or it does not exist."}, status=status.HTTP_403_FORBIDDEN)
        
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    


class ReviewPetAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, pet_id):
        pet = get_object_or_404(Pet, id=pet_id)
        user = request.user

        if not Adopt.objects.filter(user=user, pet=pet).exists():
            return Response({"error": "You can only review a pet you have adopted."}, status=status.HTTP_403_FORBIDDEN)

        data = request.data.copy()
        data['user'] = user.id
        data['pet'] = pet.id

        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PetReviewListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pet_id = self.kwargs['pk']
        return Review.objects.filter(pet_id=pet_id)

    def perform_create(self, serializer):
        pet_id = self.kwargs['pk']
        pet = get_object_or_404(Pet, id=pet_id)
        serializer.save(user=self.request.user, pet=pet)   
