from django import forms
from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('product_name', 'description', 'preview', 'category_name', 'price', 'is_published')

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        prohibited_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for obj in prohibited_list:
            if obj in cleaned_data:
                raise forms.ValidationError("Продукт запрещен на площадке")

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        prohibited_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for obj in prohibited_list:
            if obj in cleaned_data:
                raise forms.ValidationError("Продукт запрещен на площадке")

        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'name', 'number_version', 'current_version',)
