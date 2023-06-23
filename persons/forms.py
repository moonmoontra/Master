from django import forms

from persons.models import Provider


class ProviderCreateForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'