# Generated by Django 4.2.7 on 2024-01-02 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_product_bla'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bla',
        ),
    ]