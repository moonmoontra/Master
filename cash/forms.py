from django import forms
from cash.models import Valuta, Cash, Rate


class BaseCashClass(forms.ModelForm):

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