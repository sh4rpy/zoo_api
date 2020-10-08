from django.contrib import admin

from .models import Employee, ZooPlace, AnimalType, Animal


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'working_position', )
    search_fields = ('first_name', 'last_name', 'working_position', )


class ZooPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'specifications', )
    list_filter = ('name', )


class AnimalTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'place', 'responsible_employee', )
    list_filter = ('name', 'type', 'place', 'responsible_employee', )


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(ZooPlace, ZooPlaceAdmin)
admin.site.register(AnimalType, AnimalTypeAdmin)
admin.site.register(Animal, AnimalAdmin)
