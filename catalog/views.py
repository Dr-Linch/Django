from django.shortcuts import render
from django.utils.text import slugify

from catalog.models import Product, Category
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


def contacts(request):
    return render(request, 'catalog/contact.html')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'

# def index(request):
#     products_list = Product.objects.all()
#     context = {
#         'object_list': products_list,
#     }
#     return render(request, 'catalog/index.html', context)


# def product_info(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'object': product
#     }
#     return render(request, 'catalog/product.html', context)
