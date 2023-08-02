from django.urls import path

from products.views import add_product, view_product

urlpatterns = [
    path('products/add/', add_product, name='add'),
    path('products/view/', view_product, name='view'),
]