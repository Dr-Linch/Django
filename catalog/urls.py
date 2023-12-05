from django.urls import path
from catalog.views import index, contacts,product_info
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>', product_info, name='product')
]
