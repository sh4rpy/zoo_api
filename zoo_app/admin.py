from django.contrib import admin

from .models import Employee, ZooPlace, AnimalType, Animal


class EmployeeAdmin(admin.ModelAdmin):
    def get_pinned_animals(self, obj):
        return obj.animals.count()

    get_pinned_animals.short_description = 'Количество закрепленных жиивотных'
    list_display = ('first_name', 'last_name', 'age', 'working_position', 'get_pinned_animals')
    search_fields = ('first_name', 'last_name', 'working_position', )


class ZooPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'specifications', )
    list_filter = ('name', )


class AnimalTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'place', 'responsible_employee', )
    list_filter = ('name', 'type', 'place', 'responsible_employee', )
    search_fields = ('name', 'type', 'place', 'responsible_employee', )


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(ZooPlace, ZooPlaceAdmin)
admin.site.register(AnimalType, AnimalTypeAdmin)
admin.site.register(Animal, AnimalAdmin)
