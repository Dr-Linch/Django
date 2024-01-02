from django.db import models
from config import settings

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):

    product_name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='products/', null=True, blank=True)
    category_name = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField(verbose_name='цена ')
    created_date = models.DateField(auto_now_add=True, verbose_name='дата создания')
    modified_date = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')
    is_published = models.BooleanField(default=False, verbose_name='признак публикации')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'{id}, {self.product_name}, {self.price}, {self.category_name}'

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        permissions = [
            (
                'set_is_published',
                'Can public for sale'
            ),
            (
                'set_description',
                'Can edit description'
            ),
            (
                'set_category',
                'Can change category'
            )
        ]


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Название категории')
    category_description = models.TextField()

    def __str__(self):
        return f'{id}, {self.category_name}'


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='id_product')
    number_version = models.IntegerField(verbose_name='номер_версии')
    name = models.CharField(max_length=100, verbose_name='наименование')
    current_version = models.BooleanField(verbose_name='признак_текущей_версии')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
