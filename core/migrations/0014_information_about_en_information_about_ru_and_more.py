# Generated by Django 5.0 on 2024-01-13 13:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_information_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='about_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='about_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='address_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='address_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]