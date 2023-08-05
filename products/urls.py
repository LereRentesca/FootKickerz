from django.urls import path

from products.views import add_product, view_product, catalog, delete_product, product_detail

urlpatterns = [
    path('products/add/', add_product, name='add'),
    path('products/view/', view_product, name='view'),
    path('products/catalog/', catalog, name='catalog'),
    path('products/detail/<int:product_id>/', product_detail, name='detail'),
    path('products/delete/<int:product_id>/', delete_product, name='delete' ),
]