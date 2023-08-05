from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['sku','product_name','availability','brand','sport','price','description','size','image']