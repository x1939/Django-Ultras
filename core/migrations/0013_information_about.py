# Generated by Django 5.0 on 2024-01-13 13:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_blog_content_en_blog_content_ru_blog_title_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
