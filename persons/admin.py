from django.contrib import admin

from .models import Employee, Clients, Manufacturer, Provider


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'contract', 'phone', 'address')
    list_filter = ('position', 'start_date', 'end_date')


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'phone')
    list_filter = ('birthday_date',)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_filter = ('manufacturer_name', 'country')


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('provider_name', 'address', 'phone', 'status')
    list_filter = ('provider_name', 'city')