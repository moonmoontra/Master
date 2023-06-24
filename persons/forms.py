import datetime
import re
from django.utils.translation import gettext_lazy as _

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from persons.models import *
from persons.services import object_validation_only_text_field


class BaseProviderClass(forms.ModelForm):
    def clean_provider_name(self):
        provider_name = self.cleaned_data['provider_name']
        return object_validation_only_text_field(provider_name)

    class Meta:
        model = Provider
        fields = '__all__'


class BaseEmployeeClass(forms.ModelForm):
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return object_validation_only_text_field(first_name)

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return object_validation_only_text_field(last_name)

    def clean_position(self):
        position = self.cleaned_data['position']
        return object_validation_only_text_field(position)

    class Meta:
        model = Employee
        fields = '__all__'


class BaseManufacturerClass(forms.ModelForm):
    def clean_manufacturer_name(self):
        manufacturer_name = self.cleaned_data['manufacturer_name']
        return object_validation_only_text_field(manufacturer_name)

    class Meta:
        model = Manufacturer
        fields = '__all__'


class BaseClientForm(forms.ModelForm):
    def clean_client_name(self):
        client_name = self.cleaned_data['client_name']
        return object_validation_only_text_field(client_name)

    class Meta:
        model = Client
        fields = '__all__'


class ProviderCreateForm(BaseProviderClass):
    pass


class ProviderEditForm(BaseProviderClass):
    pass


class EmployeeCreateForm(BaseEmployeeClass):
    pass


class EmployeeEditForm(BaseEmployeeClass):
    pass


class ManufacturerCreateForm(BaseManufacturerClass):
    pass


class ManufacturerEditForm(BaseManufacturerClass):
    pass


class ClientCreateForm(BaseClientForm):
    pass


class ClientEditForm(BaseClientForm):
    pass
