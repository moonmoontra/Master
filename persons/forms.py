from django.forms import forms

from persons.models import Provider


class ProviderCreateForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = 'all'