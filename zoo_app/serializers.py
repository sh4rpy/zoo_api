from rest_framework import serializers

from .models import Employee, ZooPlace, AnimalType, Animal


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ZooPlaceSerializer(serializers.ModelSerializer):
    animal_count = serializers.ReadOnlyField(source='animals.count')

    class Meta:
        model = ZooPlace
        fields = '__all__'


class AnimalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalType
        fields = '__all__'


class AnimalSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='name', queryset=AnimalType.objects.all())
    place = serializers.SlugRelatedField(slug_field='name', queryset=ZooPlace.objects.all())
    # для удобства чтения добавлено поле с полным именем закрепленного сотрудника
    responsible_employee_full_name = serializers.ReadOnlyField(source='responsible_employee.get_employee_full_name')

    class Meta:
        model = Animal
        fields = '__all__'
