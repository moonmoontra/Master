from django.test import TestCase, RequestFactory
from products.models import UnitOfMeasure, PriceName
from products.views import delete_products_view
from home.services import delete_objects


class UnitOfMeasureModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.unit = UnitOfMeasure.objects.create(unit_name='Big')

    def test_unit_name_label(self):
        self.unit = UnitOfMeasure.objects.get(id=1)
        field_label = self.unit._meta.get_field('unit_name').verbose_name
        self.assertEquals(field_label, 'Назва')


class PriceNameModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.price = PriceName.objects.create(price_name='Big2')

    def test_unit_name_label(self):
        self.price = PriceName.objects.get(id=1)
        field_label = self.price._meta.get_field('price_name').verbose_name
        self.assertEquals(field_label, 'Назва')


class DeleteObjectTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_delete_object_view(self):
        request = self.factory.post(path='/products/unitofmeasures/', data={'model_name':'Unitofmeasure',
                                                                            'object_ids':['1', '1','1']})
        response = delete_products_view(request)
        self.assertEquals(response.status_code, 302)