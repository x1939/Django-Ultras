from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *

admin.site.register(Blog)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Logo)
admin.site.register(Comment)

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    search_fields = ('title',)

@admin.register(Brand)
class BrandAdmin(TranslationAdmin):
    search_fields = ('title',)

@admin.register(Information)
class InformationAdmin(TranslationAdmin):
    search_fields = ('email',)