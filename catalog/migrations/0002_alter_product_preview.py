# Generated by Django 4.2.7 on 2023-12-02 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='products/'),
        ),
    ]
