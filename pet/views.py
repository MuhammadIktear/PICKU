from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Pet, Adopt, Review, Species, Breed, Color, Size, Sex, Status
from users.models import UserAccount
from .serializers import PetSerializer, AdoptSerializer, ReviewSerializer
from filter.serializers import SpeciesSerializer, BreedSerializer, ColorSerializer, SizeSerializer, SexSerializer, StatusSerializer

class PetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class FilterOptionsAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        species = SpeciesSerializer(Species.objects.all(), many=True).data
        breed = BreedSerializer(Breed.objects.all(), many=True).data
        color = ColorSerializer(Color.objects.all(), many=True).data
        size = SizeSerializer(Size.objects.all(), many=True).data
        sex = SexSerializer(Sex.objects.all(), many=True).data
        status = StatusSerializer(Status.objects.all(), many=True).data

        return Response({
            'species': species,
            'breed': breed,
            'color': color,
            'size': size,
            'sex': sex,
            'status': status
        })


class PetAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pet_id=None):
        if pet_id:
            return self.get_detail(request, pet_id)

        queryset = Pet.objects.all().select_related('species', 'breed', 'color', 'size', 'sex', 'status')

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


class PetDetailAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [AllowAny]


class AdoptPetAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pet_id):
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


class PetUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pet_id, user):
        return get_object_or_404(Pet, id=pet_id, created_by=user)

    def put(self, request, pet_id):
        pet = self.get_object(pet_id, request.user)
        serializer = PetSerializer(pet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pet_id):
        pet = self.get_object(pet_id, request.user)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewPetAPIView(APIView):
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pet_id = self.kwargs['pk']
        return Review.objects.filter(pet_id=pet_id)

    def perform_create(self, serializer):
        pet_id = self.kwargs['pk']
        pet = get_object_or_404(Pet, id=pet_id)
        serializer.save(user=self.request.user, pet=pet)