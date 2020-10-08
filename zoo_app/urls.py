from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employees')
router.register('zoo_places', views.ZooPlaceViewSet, basename='zoo_places')
router.register('animal_types', views.AnimalTypeViewSet, basename='animal_types')
router.register('animals', views.AnimalViewSet, basename='animals')
urlpatterns = [
    path('', include(router.urls))
]
