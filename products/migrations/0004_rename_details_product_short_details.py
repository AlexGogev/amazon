# Generated by Django 4.0.3 on 2022-03-30 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_full_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='details',
            new_name='short_details',
        ),
    ]