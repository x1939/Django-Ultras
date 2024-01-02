from modeltranslation.translator import translator, TranslationOptions
from .models import *

class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

translator.register(Blog, BlogTranslationOptions)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Category, CategoryTranslationOptions)

class BrandTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Brand, BrandTranslationOptions)

class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Product, ProductTranslationOptions)