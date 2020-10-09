from rest_framework import viewsets

from .models import Employee, ZooPlace, AnimalType, Animal
from .serializers import EmployeeSerializer, ZooPlaceSerializer, AnimalTypeSerializer, AnimalSerializer
from .filters import ZooPlaceFilter, AnimalFilter


class EmployeeViewSet(viewsets.ModelViewSet):
    """Представление сотрудников зоопарка"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_fields = ('working_position', )
    ordering_fields = ('first_name', 'last_name', )


class ZooPlaceViewSet(viewsets.ModelViewSet):
    """Представление места животного в зоопарке"""
    queryset = ZooPlace.objects.all()
    serializer_class = ZooPlaceSerializer
    filterset_class = ZooPlaceFilter
    filterset_fields = ('name', )
    ordering_fields = ('name', )


class AnimalTypeViewSet(viewsets.ModelViewSet):
    """Представление вида животного"""
    queryset = AnimalType.objects.all()
    serializer_class = AnimalTypeSerializer
    filterset_fields = ('name', )
    ordering_fields = ('name', )


class AnimalViewSet(viewsets.ModelViewSet):
    """Представление животного"""
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    filterset_class = AnimalFilter
    filterset_fields = ('name', 'type', 'place', 'responsible_employee', )
    ordering_fields = ('name', 'type', 'place', )
