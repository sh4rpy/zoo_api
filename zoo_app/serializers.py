from rest_framework import serializers

from .models import Employee, ZooPlace, AnimalType, Animal


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ZooPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZooPlace
        fields = '__all__'


class AnimalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalType
        fields = '__all__'


class AnimalSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='type.name')
    place = serializers.CharField(source='place.name')
    responsible_employee = serializers.CharField(source='responsible_employee.__str__')

    class Meta:
        model = Animal
        fields = '__all__'
