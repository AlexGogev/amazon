# Generated by Django 4.0.3 on 2022-03-30 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='full_detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]