from django import forms
from documents.models import Document, ProductInDocument


class BaseDocumentClass(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BaseDocumentClass, self).__init__(*args, **kwargs)
        self.fields['document_type'].empty_label = None
        self.fields['provider'].empty_label = None
        self.fields['stock'].empty_label = None
        self.fields['price_name'].empty_label = None
        self.fields['valuta'].empty_label = None
        self.fields['cash'].empty_label = None

    class Meta:
        model = Document
        fields = ['document_type', 'provider', 'stock', 'price_name', 'valuta', 'cash']


class BaseProductInDocumentClass(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BaseProductInDocumentClass, self).__init__(*args, **kwargs)
        self.fields['document'].disabled = True
        self.fields['product'].empty_label = None

    class Meta:
        model = ProductInDocument
        fields = ['document', 'product', 'count', 'price']


class DocumentForm(BaseDocumentClass):
    pass


class ProductInDocumentForm(BaseProductInDocumentClass):
    pass


class DocumentHoldForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['hold']