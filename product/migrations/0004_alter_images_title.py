# Generated by Django 4.1.2 on 2022-12-14 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_category_title_alter_product_title_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
