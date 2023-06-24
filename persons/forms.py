import datetime
import re
from django.utils.translation import gettext_lazy as _

from django import forms
from django.core.exceptions import ValidationError
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
    def clean_client_name(self):
        client_name = self.cleaned_data['client_name']

        if not re.match(r'^[a-zA-ZА-Яа-яЁёЇїІіЄєҐґ\s]+$', client_name):
            raise ValidationError(_('Ім\'я не може містити цифри!'))

        return client_name

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if not re.match(r'^[+]?\d+', phone):
            raise ValidationError(_('Некоректний номер телефону!'))

        return phone

    class Meta:
        model = Clients
        fields = '__all__'


class ClientEditForm(forms.ModelForm):
    def clean_client_name(self):
        client_name = self.cleaned_data['client_name']

        if not re.match(r'^[a-zA-ZА-Яа-яЁёЇїІіЄєҐґ\s]+$', client_name):
            raise ValidationError(_('Ім\'я не може містити цифри!'))

        return client_name

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if not re.match(r'^[+]?\d+', phone):
            raise ValidationError(_('Некоректний номер телефону!'))

        return phone

    class Meta:
        model = Clients
        fields = '__all__'