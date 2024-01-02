from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *

admin.site.register(Contact)
admin.site.register(Brand)
admin.site.register(Information)
admin.site.register(Logo)
admin.site.register(Comment)

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    search_fields = ('title',)

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    search_fields = ('title',)

@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    search_fields = ('title',)