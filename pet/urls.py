from django.urls import path
from .views import PetListCreateAPIView, PetListAPIView, PetDetailAPIView, AdoptPetAPIView, ReviewPetAPIView,PetUpdateAPIView

urlpatterns = [
    path('pets/', PetListAPIView.as_view(), name='pet-list'),
    path('pets/create/', PetListCreateAPIView.as_view(), name='pet-create'),
    path('pets/<int:pk>/', PetDetailAPIView.as_view(), name='pet-detail'),
    path('adopt/<int:pet_id>/', AdoptPetAPIView.as_view(), name='adopt-pet'),
    path('review/<int:pet_id>/', ReviewPetAPIView.as_view(), name='review-pet'),
    path('pets/<int:pet_id>/update/', PetUpdateAPIView.as_view(), name='pet-update'),
]
