from django import forms
from cashes.models import Valuta, Cash, Rate


class BaseCashClass(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BaseCashClass, self).__init__(*args, **kwargs)
        self.fields['valuta'].empty_label = None

    class Meta:
        model = Cash
        fields = '__all__'


class BaseValutaClass(forms.ModelForm):

    class Meta:
        model = Valuta
        fields = '__all__'


class BaseRateClass(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BaseRateClass, self).__init__(*args, **kwargs)
        self.fields['valuta'].empty_label = None

    class Meta:
        model = Rate
        fields = '__all__'


class CashForm(BaseCashClass):
    pass


class ValutaForm(BaseValutaClass):
    pass


class RateForm(BaseRateClass):
    pass