from django.urls import path
from catalog.views import contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
]
