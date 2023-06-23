from django import forms

from persons.models import Provider


# class CreateProviderService(Service):
#     provider_name = forms.CharField()
#     city = forms.CharField()
#     address = forms.CharField()
#     phone = forms.CharField()
#     status = forms.CharField()
#
#     def process(self):
#         provider_name = self.cleaned_data['provider_name']
#         city = self.cleaned_data['city']
#         address = self.cleaned_data['address']
#         phone = self.cleaned_data['phone']
#         status = self.cleaned_data['status']
#
#         # provider = Provider.objects.update_or_create(
#         #     provider_name=provider_name,
#         #     city=city,
#         #     address=address,
#         #     phone=phone,
#         #     status=status
#         # )
#
#         self.privider = Provider.objects.create(
#             provider_name=provider_name,
#             city=city,
#             address=address,
#             phone=phone,
#             status=status,
#         )
#
#         return self.privider

def filter_objects_delete(objects, list, **kwargs):
    return objects.filter(id__in=list, **kwargs).delete()