# Generated by Django 5.0 on 2024-01-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_information_address_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_basket_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
