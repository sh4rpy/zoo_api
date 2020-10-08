from rest_framework import viewsets

from .models import Employee, ZooPlace, AnimalType, Animal
from .serializers import EmployeeSerializer, ZooPlaceSerializer, AnimalTypeSerializer, AnimalSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_fields = ('working_position', )
    ordering_fields = ('first_name', 'last_name', )


class ZooPlaceViewSet(viewsets.ModelViewSet):
    queryset = ZooPlace.objects.all()
    serializer_class = ZooPlaceSerializer
    filterset_fields = ('name',)
    ordering_fields = ('name', )


class AnimalTypeViewSet(viewsets.ModelViewSet):
    queryset = AnimalType.objects.all()
    serializer_class = AnimalTypeSerializer
    filterset_fields = ('name', )
    ordering_fields = ('name', )


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    filterset_fields = ('name', 'type', 'place', 'responsible_employee', )
    ordering_fields = ('name', 'type', 'place', )
