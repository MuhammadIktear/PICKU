from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Pet, Adopt, Review
from users.models import UserAccount
from .serializers import PetSerializer, AdoptSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

class PetAPIView(APIView):
    permission_classes = [AllowAny]  # Adjust permissions as needed

    def get(self, request, pet_id=None):
        if pet_id:
            return self.get_detail(request, pet_id)

        queryset = Pet.objects.all()

        # Filter pets based on query parameters
        species = request.query_params.get('species')
        breed = request.query_params.get('breed')
        color = request.query_params.get('color')
        size = request.query_params.get('size')
        sex = request.query_params.get('sex')
        status = request.query_params.get('status')

        if species:
            queryset = queryset.filter(species__name=species)
        if breed:
            queryset = queryset.filter(breed__name=breed)
        if color:
            queryset = queryset.filter(color__name=color)
        if size:
            queryset = queryset.filter(size__name=size)
        if sex:
            queryset = queryset.filter(sex__name=sex)
        if status:
            queryset = queryset.filter(status__name=status)

        serializer = PetSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, pet_id=None):
        if pet_id:
            return Response({"error": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    def get_detail(self, request, pet_id):
        pet = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(pet)
        return Response(serializer.data)

    def get_object(self, pet_id, user):
        try:
            pet = Pet.objects.get(id=pet_id, created_by=user)
            return pet
        except Pet.DoesNotExist:
            return None

    def post_adopt(self, request, pet_id):
        pet = get_object_or_404(Pet, id=pet_id)
        user = request.user
        bank_account = get_object_or_404(UserAccount, user=user)

        if pet.status != 'Available To Adopt':
            return Response({"error": "This pet is not available for adoption."}, status=status.HTTP_400_BAD_REQUEST)

        if bank_account.balance < pet.rehoming_fee:
            return Response({"error": "Insufficient balance."}, status=status.HTTP_400_BAD_REQUEST)

        bank_account.balance -= pet.rehoming_fee
        bank_account.save()

        adoption = Adopt.objects.create(user=user, pet=pet)
        serializer = AdoptSerializer(adoption)

        pet.status = 'Adopted'
        pet.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post_review(self, request, pet_id):
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
