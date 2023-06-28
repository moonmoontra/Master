from django import forms
from home.services import object_validation_only_text_field
from persons.forms import ObjectValidationMixin
from products.models import ProductRefBook, UnitOfMeasure, ProductPriceName, PriceName


class BaseProductRefBookClass(forms.ModelForm, ObjectValidationMixin):

    class Meta:
        model = ProductRefBook
        fields = '__all__'


class BaseUnitOfMeasureClass(forms.ModelForm, ObjectValidationMixin):

    class Meta:
        model = UnitOfMeasure
        fields = '__all__'


class BaseProductPriceNameClass(forms.ModelForm):

    class Meta:
        model = ProductPriceName
        fields = '__all__'


class BasePriceNameClass(forms.ModelForm):

    class Meta:
        model = PriceName
        fields = '__all__'


class ProductRefBookForm(BaseProductRefBookClass):
    pass


class UnitOfMeasureForm(BaseUnitOfMeasureClass):
    pass


class ProductPriceNameForm(BaseProductPriceNameClass):
    pass


class PriceNameForm(BasePriceNameClass):
    pass