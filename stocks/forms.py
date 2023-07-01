from django import forms
from stocks.models import Stock


class BaseStockClass(forms.ModelForm):

        class Meta:
            model = Stock
            fields = '__all__'


class StockForm(BaseStockClass):
    pass