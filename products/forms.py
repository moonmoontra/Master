import re
from django import forms
from home.services import object_validation_only_text_field
from persons.forms import ObjectValidationMixin
from products.models import ProductRefBook, UnitOfMeasure, ProductPriceName, PriceName
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class BaseProductRefBookClass(forms.ModelForm):

    def clean_articul(self):
        articul = self.cleaned_data['articul']
        regex = r'^[A-Z0-9-]+$'
        if not re.match(regex, articul):
            raise ValidationError(_('Введіть коректне значення!'))
        else:
            return articul

    def __init__(self, *args, **kwargs):
        super(BaseProductRefBookClass, self).__init__(*args, **kwargs)
        self.fields['manufacturer'].empty_label = None
        self.fields['unitOfMeasure'].empty_label = None

    class Meta:
        model = ProductRefBook
        fields = '__all__'


class BaseUnitOfMeasureClass(forms.ModelForm, ObjectValidationMixin):

    def clean_unit_name(self):
        unit_name = self.cleaned_data['unit_name']
        regex = r'^[0-9А-ЯЁа-яё. ]+$'
        if not re.match(regex, unit_name):
            raise ValidationError(_('Введіть коректне значення!'))
        else:
            return unit_name

    class Meta:
        model = UnitOfMeasure
        fields = '__all__'


class BaseProductPriceNameClass(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BaseProductPriceNameClass, self).__init__(*args, **kwargs)
        self.fields['product'].empty_label = None
        self.fields['price'].empty_label = None
        self.fields['unitOfMeasure'].empty_label = None

    class Meta:
        model = ProductPriceName
        fields = '__all__'


class BasePriceNameClass(forms.ModelForm, ObjectValidationMixin):

    def clean_price_name(self):
        return self.clean_field('price_name')

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