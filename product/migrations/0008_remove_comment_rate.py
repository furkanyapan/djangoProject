# Generated by Django 4.1.2 on 2022-12-18 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='rate',
        ),
    ]