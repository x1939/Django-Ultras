from django.contrib import admin
from .models import *

admin.site.register(Contact)
admin.site.register(Brand)
admin.site.register(Information)
admin.site.register(Logo)
admin.site.register(Comment)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('title',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    search_fields = ('title',)