from django import forms
from django.core.validators import RegexValidator

from persons.models import *


class ProviderCreateForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'

class ProviderEditForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeEditForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class ManufacturerCreateForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class ManufacturerEditForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class ClientCreateForm(forms.ModelForm):
    client_name = forms.CharField(max_length=30, required=True, validators=[RegexValidator(regex=r'^[a-zA-ZА-Яа-яЁёЇїІіЄєҐґ\s]+$')])
    phone = forms.CharField(max_length=15, required=True, validators=[RegexValidator(regex=r'^[+]?\d+')])
    birthday_date = forms.DateField(required=True)
    class Meta:
        model = Clients
        fields = '__all__'


class ClientEditForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'