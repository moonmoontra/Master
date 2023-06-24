from django import forms

from persons.models import *


class ProviderCreateForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'


class EmployeeCreateForm(forms.ModelForm):
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


class ProviderEditForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'