from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import *
from basket.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

class ProductView(LoginRequiredMixin,ListView):
    """Отображение списка покупок"""
    template_name = 'basket/list-product.html'

    def get_queryset(self):
        obj = ProductList.objects.filter(user=self.request.user)
        return obj


class AddProduct(CreateView):
    """Добаление продукта в список покупок"""
    model = ProductList
    template_name = 'basket/add.html'
    form_class = AddForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = AddForm()
        form.fields["category"].queryset = Category.objects.filter(user=self.request.user)
        context["form"] = form
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('/')

    def success_url(self):
        return redirect('/')


class UpdateProduct(UpdateView):
    """Редактирование продукта, что бы отредактировать нажмите на продукт"""
    model = ProductList
    template_name = 'basket/update.html'
    form_class = AddForm


class DeleteProduct(DeleteView):
    """Удаление товара"""
    model = ProductList
    template_name = 'basket/delete.html'
    success_url = '/'


class SortView(View):
    """Сортировка в алфавитном порядке и по дате,
    для сортировки по алфавиту нажмите на "Товары",
    для сортировки по дате нажмите на "Дата".
    """

    def get(self, request, pk):
        if pk == 1:
            products = ProductList.objects.filter(user=request.user).order_by("item")
        elif pk == 2:
            products = ProductList.objects.filter(user=request.user).order_by("date")
        return render(request, 'basket/list-product.html', {"object_list": products})


class CategoryView(ListView):
    """Отображение списка категорий """
    template_name = 'basket/category.html'

    def get_queryset(self):
        obj = Category.objects.all()
        return obj


class AddCategory(CreateView):
    """Добаление продукта в список покупок"""
    model = Category
    template_name = 'basket/addcategory.html'
    form_class = AddCategoryForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('/')

    def success_url(self):
        return redirect('/')


class CategorySort(View):
    """Фильтрация по категориям при нажатии на категорию"""
    def get(self, request, slug):
        product = ProductList.objects.filter(category__slug=slug)
        context = {
            'product': product
        }
        return render(request, 'basket/categorysort.html', context)