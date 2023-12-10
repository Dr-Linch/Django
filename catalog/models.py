from django.db import models


# Create your models here.


class Product(models.Model):

    product_name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='products/', null=True, blank=True)
    category_name = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField(verbose_name='цена ')
    created_date = models.DateField(verbose_name='дата создания')
    modified_date = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{id}, {self.product_name}, {self.price}, {self.category_name}'

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Название категории')
    category_description = models.TextField()

    def __str__(self):
        return f'{id}, {self.category_name}'
