from django.contrib import admin

from backend.models.officials import Official
from backend.models.persons import Person
from backend.models.vehicles import Vehicle


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'email']
    search_fields = ['first_name', 'last_name', 'email']


@admin.register(Official)
class OfficialAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'code']
    search_fields = ['first_name', 'last_name', 'code']
    readonly_fields = ['code', 'user']


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['plate_number', 'brand', 'color', 'person']
    search_fields = ['plate_number', 'brand', 'color', 'person']
