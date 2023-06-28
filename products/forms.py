from django import forms
from home.services import object_validation_only_text_field
from products.models import ProductRefBook, UnitOfMeasure, ProductPriceName


class BaseProductRefBookClass(forms.ModelForm):

    class Meta:
        model = ProductRefBook
        fields = '__all__'


class BaseUnitOfMeasureClass(forms.ModelForm):

    class Meta:
        model = UnitOfMeasure
        fields = '__all__'


class BaseProductPriceNameClass(forms.ModelForm):

    class Meta:
        model = ProductPriceName
        fields = '__all__'


class ProductRefBookForm(BaseProductRefBookClass):
    pass


class UnitOfMeasureForm(BaseUnitOfMeasureClass):
    pass


class ProductPriceNameForm(BaseProductPriceNameClass):
    pass