from django import forms
from .models import ProductList, Category


class AddForm(forms.ModelForm):
    class Meta:
        model = ProductList
        exclude = ('user', 'slug',)


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('parent', 'slug', 'user',)
