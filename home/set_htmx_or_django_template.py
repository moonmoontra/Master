""" CustomHtmxMixin - класс, добавляющий в представление возможность отображения в виде htmx-блока.
template_htmx - имя шаблона, используемого для отображения представления в виде htmx-блока.
template_name - имя шаблона, используемого для отображения представления.
dispatch - метод, вызываемый при обращении к представлению.
HTTP_HX_REQUEST - заголовок, по которому определяется, является ли запрос htmx-запросом.
Если запрос не является htmx-запросом, то в качестве шаблона для отображения представления
используется шаблон home\include_base_block.html.
Если запрос является htmx-запросом, то в качестве шаблона для отображения представления
используется шаблон, указанный в атрибуте template_htmx. """


class CustomHtmxMixin:
    def dispatch(self, request, *args, **kwargs):
        self.template_htmx = self.template_name
        if not self.request.META.get('HTTP_HX_REQUEST'):
            self.template_name = 'home/include_base_block.html'

        return super().dispatch(request, *args, **kwargs)
