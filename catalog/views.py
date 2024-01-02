from django.shortcuts import render, redirect, reverse
from django.forms import inlineformset_factory
from django.utils.text import slugify
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Category, Version
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from catalog.services import get_cache_category


def contacts(request):
    return render(request, 'catalog/contact.html')


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    extra_context = {
        'title': 'SkyStore - Магазин и Блог, Блогазин, Магалог'
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['category_list'] = get_cache_category()
        return context_data


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/index.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for product in context['object_list']:
            active_version = product.version_set.filter(current_version=True).first()
            if active_version:
                product.active_version_number = active_version.number_version
                product.active_title = active_version.name
            else:
                product.active_version_number = ''
                product.active_title = 'Доступна тестовая версия'

        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = context['object']

        active_version = product.version_set.filter(current_version=True).last()
        if active_version:
            product.active_version_number = active_version.number_version
            product.active_version_name = active_version.name
        else:
            product.active_version_number = None
            product.active_version_name = None

        return context


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method =='POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method =='POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if self.object.owner != self.request.user:
            return redirect(reverse('users:login'))
        else:
            self.object.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
            return super().form_valid(form)

    def test_func(self):
        _user = self.request.user
        _instance: Product = self.get_object()
        custom_perms: tuple = (
            'catalog.set_is_published',
            'catalog.set_category',
            'catalog.set_description',
        )
        print(_user.groups.all())
        print(_user.is_superuser)
        if _user == _instance.owner:
            print('owner')
            return True
        elif _user.is_superuser:
            print('superuser')
            return True
        elif _user.groups.filter(name='moderators') and _user.has_perms(custom_perms):
            print('moderator')
            return True
        else:
            print('no permissions')
            return self.handle_no_permission()
