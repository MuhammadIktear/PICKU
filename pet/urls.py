from django.urls import path
from .views import PetAPIView

urlpatterns = [
    path('pets/', PetAPIView.as_view(), name='pet-list-create'),
    path('pets/<int:pet_id>/', PetAPIView.as_view(), name='pet-detail'),
    path('pets/<int:pet_id>/adopt/', PetAPIView.as_view(), name='pet-adopt'),
    path('pets/<int:pet_id>/review/', PetAPIView.as_view(), name='pet-review'),
]
