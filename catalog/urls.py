from django.urls import path
from catalog.views import contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, CategoryListView
from catalog.apps import CatalogConfig
from django.views.decorators.cache import cache_page, never_cache


app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>', cache_page(30)(ProductDetailView.as_view()), name='product'),
    path('create/', never_cache(ProductCreateView.as_view()), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('categorys/', CategoryListView.as_view(), name='categorys'),
]
