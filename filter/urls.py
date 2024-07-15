# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpeciesViewSet, BreedViewSet, ColorViewSet, SizeViewSet, SexViewSet, StatusViewSet

router = DefaultRouter()
router.register(r'species', SpeciesViewSet)
router.register(r'breeds', BreedViewSet)
router.register(r'colors', ColorViewSet)
router.register(r'sizes', SizeViewSet)
router.register(r'sexes', SexViewSet)
router.register(r'statuses', StatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
