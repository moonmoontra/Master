from django.views.generic import CreateView, UpdateView
from home.base_view import BaseListView, BaseCreateEditMixin
from home.services import delete_objects
from home.set_htmx_or_django_template import CustomHtmxMixin
from products.forms import UnitOfMeasureForm, ProductRefBookForm, ProductPriceNameForm, PriceNameForm
from products.models import PriceName, ProductPriceName, UnitOfMeasure, ProductRefBook
from django.apps import apps


""" BaseProductView - базовый класс для представлений, связанных с моделями, относящимися к продуктам.
    template_name - имя шаблона, используемого для отображения представления.
    model - модель, с которой работает представление.
    form_class - форма, используемая для создания и редактирования объектов модели.
    success_url - URL, на который будет перенаправлен пользователь после успешного выполнения операции.
    get_success_url() - метод, который возвращает URL, на который будет перенаправлен пользователь после 
    успешного выполнения операции."""


class BaseProductView:
    template_name = None
    model = None
    form_class = None
    success_url = '/products/'

    def get_success_url(self):
        return self.success_url + self.model.__name__.lower() + 's'


""" BaseCreateView - базовый класс для представлений, связанных с моделями, относящимися к продуктам
    и использующих форму для создания объектов модели."""


class BaseCreateView(BaseCreateEditMixin, BaseProductView, CreateView):
    pass


"""BaseEditView - базовый класс для представлений, связанных с моделями, относящимися к продуктам
    и использующих форму для редактирования объектов модели."""


class BaseEditView(BaseCreateEditMixin, BaseProductView, UpdateView):
    pass


"""ProductRefBookListView - представление для отображения списка справочника продуктов.
    model - модель, с которой работает представление.
    template_name - имя шаблона, используемого для отображения представления.
    edit_view_name - имя представления для редактирования объекта модели.
    delete_view_name - имя представления для удаления объекта модели."""


class ProductRefBookListView(CustomHtmxMixin, BaseListView, BaseProductView):
    model = ProductRefBook
    template_name = 'products/product_ref_book_list.html'
    edit_view_name = 'product_ref_book_edit'
    delete_view_name = 'delete_product'
    create_view_name = 'product_ref_book_create'
    title = 'Товари'


class ProductRefBookEditView(CustomHtmxMixin, BaseEditView):
    form_class = ProductRefBookForm
    model = ProductRefBook
    template_name = 'products/product_ref_book_edit.html'


class ProductRefBookCreateView(CustomHtmxMixin, BaseCreateView):
    form_class = ProductRefBookForm
    model = ProductRefBook
    template_name = 'products/product_ref_book_create.html'


class ProductPriceNameListView(CustomHtmxMixin, BaseListView, BaseProductView):
    model = ProductPriceName
    template_name = 'products/product_price_list.html'
    edit_view_name = 'product_price_edit'
    delete_view_name = 'delete_product'
    create_view_name = 'product_price_create'
    title = 'Ціни товарів'


class ProductPriceNameCreateView(CustomHtmxMixin, BaseCreateView):
    form_class = ProductPriceNameForm
    model = ProductPriceName
    template_name = 'products/product_price_create.html'


class ProductPriceNameEditView(CustomHtmxMixin, BaseEditView):
    form_class = ProductPriceNameForm
    model = ProductPriceName
    template_name = 'products/product_price_edit.html'


class UnitOfMeasureListView(CustomHtmxMixin, BaseListView, BaseProductView):
    model = UnitOfMeasure
    template_name = 'products/unit_of_measure_list.html'
    edit_view_name = 'unit_of_measure_edit'
    delete_view_name = 'delete_product'
    create_view_name = 'unit_of_measure_create'
    title = 'Одиниці виміру'


class UnitOfMeasureCreateView(CustomHtmxMixin, BaseCreateView):
    form_class = UnitOfMeasureForm
    model = UnitOfMeasure
    template_name = 'products/unit_of_measure_create.html'


class UnitOfMeasureEditView(CustomHtmxMixin, BaseEditView):
    form_class = UnitOfMeasureForm
    model = UnitOfMeasure
    template_name = 'products/unit_of_measure_edit.html'


class PriceNameListView(CustomHtmxMixin, BaseListView, BaseProductView):
    model = PriceName
    template_name = 'products/price_name_list.html'
    edit_view_name = 'price_name_edit'
    delete_view_name = 'delete_product'
    create_view_name = 'price_name_create'
    title = 'Назви цін'


class PriceNameCreateView(CustomHtmxMixin, BaseCreateView):
    form_class = PriceNameForm
    model = PriceName
    template_name = 'products/price_name_create.html'


class PriceNameEditView(CustomHtmxMixin, BaseEditView):
    form_class = PriceNameForm
    model = PriceName
    template_name = 'products/price_name_edit.html'


def delete_products_view(request):
    model_name = request.POST.get('model_name')
    model = apps.get_model('products', model_name)
    return delete_objects(request, model)
