from django.db import models


class Employee(models.Model):
    """Работник"""
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    working_position = models.CharField(max_length=50, verbose_name='Должность')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавлениия')
    updated_at = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class ZooPlace(models.Model):
    """Место в зоопарке"""
    name = models.CharField(max_length=50, verbose_name='Названиие')
    specifications = models.TextField(verbose_name='Характеристики')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавлениия')
    updated_at = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name


class AnimalType(models.Model):
    """Вид животного"""
    name = models.CharField(max_length=50, verbose_name='Названиие')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавлениия')
    updated_at = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name


class Animal(models.Model):
    """Животное"""
    name = models.CharField(max_length=50, verbose_name='Название')
    type = models.ForeignKey(AnimalType, verbose_name='Вид', on_delete=models.CASCADE, related_name='animal_type')
    place = models.ForeignKey(ZooPlace, verbose_name='Место', on_delete=models.CASCADE, related_name='animal_place')
    responsible_employee = models.ForeignKey(Employee, verbose_name='Ответсвтенный', on_delete=models.CASCADE,
                                             related_name='animal_employee')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавлениия')
    updated_at = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name
