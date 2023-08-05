from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product, Sport, Brand
from django.shortcuts import get_object_or_404
# Create your views here.
@login_required
def view_product(request):
    products = Product.objects.all()
    return render(request, 'products/view.html',{
        'products':products
    })

def view_product_by_brand(request):
    products = Product.objects.filter(brand_id=request.POST)
    return render(request, 'products/view.html',{
        'products':products
    })

@login_required
def product_detail(request, product_id):
    if request.method == 'GET':
        product = get_object_or_404(Product, sku=product_id)
        form = ProductForm(instance=product)
        return render(request, 'products/detail.html',{
            'product':product,
            'form':form
        })
    else:
        try:
            product = get_object_or_404(Product, sku=product_id)
            form = ProductForm(request.POST, instance=product)
            print(form)
            form.save()
            return redirect('view')
        except ValueError:
            return render(request, 'products/detail.html',{
                'product':product,
                'form':form,
                'error':'Error updating product'
            })

def catalog(request):
    brand = request.POST.get('brand-jordan', None)
    single_object = get_object_or_404(Brand, name=brand)
    catalog = Product.objects.filter(brand=single_object)
    print(catalog)
    print(single_object.pk)
    return render(request, 'products/catalog.html', {
        'form':brand,
        'products':catalog,
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
            s1 = Sport.objects.get(id=request.POST['sport'])
            b1 = Brand.objects.get(id=request.POST['brand'])
            product = Product(
                sku=request.POST['sku'],
                product_name=request.POST['product_name'],
                availability=flag,
                brand=b1,
                sport=s1,
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
        
@login_required
def delete_product(request, product_id):
    product = Product.objects.get(sku=product_id)
    product.delete()
    return redirect('view')