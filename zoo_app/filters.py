from datetime import datetime, timedelta

import django_filters
from django.db.models import Count

from .models import ZooPlace, Animal


def get_places_with_two_animals(queryset, name, value):
    """Получаем места в зоопарке, где содержатся минимум два животных"""
    return queryset.annotate(animals_count=Count('animals')).filter(animals_count__gte=2)


def get_animals_with_experienced_employee(queryset, name, value):
    """Получаем животных, за которымии закреплен работник более одного года"""
    experience = datetime.now() - timedelta(days=365)
    return queryset.filter(appointment_employee_at__lt=experience)


class ZooPlaceFilter(django_filters.FilterSet):
    """Фильтр для мест в зоопарке"""
    animal_count = django_filters.BooleanFilter(method=get_places_with_two_animals,
                                                label='Учитывать кол-во животных?')

    class Meta:
        model = ZooPlace
        fields = ('name', 'animal_count',)


class AnimalFilter(django_filters.FilterSet):
    """Фильтр для животных"""
    experience = django_filters.BooleanFilter(method=get_animals_with_experienced_employee,
                                              label='Учитывать опыт работника?')
    place_specifications = django_filters.CharFilter(field_name='place__specifications', lookup_expr='icontains')

    class Meta:
        model = Animal
        fields = ('name', 'type', 'place', 'responsible_employee', 'experience', 'place_specifications',)
