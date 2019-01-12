from django.urls import path
from basket.views import *

urlpatterns = [
    path('', ProductView.as_view(), name="product_list"),
    path('add/', AddProduct.as_view(), name='add'),
    path('update/<slug:slug>/', UpdateProduct.as_view(), name='update'),
    path('delete/<slug:slug>/', DeleteProduct.as_view(), name='delete'),
    path('sort/<int:pk>/', SortView.as_view(), name='sort'),
    path('category/', CategoryView.as_view(), name='category'),
    path('addcategory/', AddCategory.as_view(), name='addcategory'),
    path('sortcategory/<slug:slug>/', CategorySort.as_view(), name='sortcategory'),
]
