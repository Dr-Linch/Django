# Generated by Django 4.2.7 on 2023-12-22 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_article_alter_category_category_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
    ]
