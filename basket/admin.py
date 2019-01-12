from django.contrib import admin
from basket.models import Category, ProductList


class ProductAdmin(admin.ModelAdmin):
    """Отображение продуктов в админке"""
    list_display = ('user', 'item', 'category', 'date',)
    prepopulated_fields = {"slug": ("item",)}


admin.site.register(Category)
admin.site.register(ProductList, ProductAdmin)
