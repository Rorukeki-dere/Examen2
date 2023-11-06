# Generated by Django 4.2.6 on 2023-10-31 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='Generic Product Description', max_length=256),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(default='Generic Product Name', max_length=32),
        ),
    ]