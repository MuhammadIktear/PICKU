from django.urls import path
from .views import PetListCreateAPIView, PetAPIView, PetDetailAPIView, AdoptPetAPIView, ReviewPetAPIView,PetUpdateAPIView,PetReviewListCreateAPIView,FilterOptionsAPIView

urlpatterns = [
    path('pets/', PetAPIView.as_view(), name='pet-list'),
    path('pets/create/', PetListCreateAPIView.as_view(), name='pet-create'),
    path('pets/<int:pk>/', PetDetailAPIView.as_view(), name='pet-detail'),
    path('pets/adopt/<int:pet_id>/', AdoptPetAPIView.as_view(), name='adopt-pet'),
    path('pets/review/<int:pet_id>/', ReviewPetAPIView.as_view(), name='review-pet'),
    path('pets/<int:pet_id>/update/', PetUpdateAPIView.as_view(), name='pet-update'),
    path('pets/<int:pet_id>/reviews/', PetReviewListCreateAPIView.as_view(), name='pet-review-list-create'),
    path('pets/filters/', FilterOptionsAPIView.as_view(), name='pet-filters'),
]