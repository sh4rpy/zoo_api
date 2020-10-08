import django_filters
from django.db.models import Count

from .models import ZooPlace


def get_places_with_two_animals(queryset, name, value):
    return queryset.annotate(animals_count=Count('animals')).filter(animals_count__gte=value)


class AnimalPlaceFilter(django_filters.FilterSet):
    animal_count = django_filters.CharFilter(method=get_places_with_two_animals, label='Кол-во животных')

    class Meta:
        model = ZooPlace
        fields = ('name', 'animal_count', )
