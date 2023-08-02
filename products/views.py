from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product

# Create your views here.
@login_required
def view_product(request):
    products = Product.objects.all()
    return render(request, 'products/view.html',{
        'products':products
    })


@login_required
def add_product(request):
    if request.method == 'GET':
        return render(request, 'products/add.html',{
            'form':ProductForm
        })
    else:
        try:
            if request.POST['availability'] == 'on':
                flag = True
            else:
                flag = False
            product = Product(
                sku=request.POST['sku'],
                product_name=request.POST['product_name'],
                availability=flag,
                price=request.POST['price'],
                description=request.POST['description'],
                size=request.POST['size'],
                image=request.FILES['image'],
            )
            product.save()
            return redirect('view')
        except:
            return render(request, 'products/add.html',{
                'form':ProductForm,
                'error':'Please provide valid data'
            })