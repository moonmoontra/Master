from django import forms
from django_select2.forms import Select2Widget

from persons.models import *
from home.services import object_validation_only_text_field


class ObjectValidationMixin:
    def clean_field(self, field_name):
        field_value = self.cleaned_data[field_name]
        return object_validation_only_text_field(field_value)


class BaseProviderClass(ObjectValidationMixin, forms.ModelForm):
    def clean_provider_name(self):
        return self.clean_field('provider_name')

    class Meta:
        model = Provider
        fields = '__all__'


class BaseEmployeeClass(ObjectValidationMixin, forms.ModelForm):
    def clean_first_name(self):
        return self.clean_field('first_name')

    def clean_last_name(self):
        return self.clean_field('last_name')

    def clean_position(self):
        return self.clean_field('position')

    class Meta:
        model = Employee
        fields = '__all__'


class BaseManufacturerClass(ObjectValidationMixin, forms.ModelForm):
    def clean_manufacturer_name(self):
        return self.clean_field('manufacturer_name')

    class Meta:
        model = Manufacturer
        fields = '__all__'


class BaseClientForm(ObjectValidationMixin, forms.ModelForm):
    def clean_client_name(self):
        return self.clean_field('client_name')

    class Meta:
        model = Client
        fields = '__all__'


class ProviderForm(BaseProviderClass):
    pass


class EmployeeForm(BaseEmployeeClass):
    pass


class ManufacturerForm(BaseManufacturerClass):
    pass


class ClientForm(BaseClientForm):
    pass
