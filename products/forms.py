from django import forms
from home.services import object_validation_only_text_field
from products.models import ProductRefBook


class BaseProductRefBookClass(forms.ModelForm):

    class Meta:
        model = ProductRefBook
        fields = '__all__'


class ProductRefBookForm(BaseProductRefBookClass):
    pass