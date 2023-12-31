from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def cart(request):
    return render(request, 'pages/cart.html')

def contact(request):
    return render(request, 'pages/contact.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'registration/signup_new.html',{
            'form':UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                        password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'registration/signup_new.html',{
                    'form':UserCreationForm,
                    'error':'Username already exists'
                })
        return render(request, 'registration/signup_new.html',{
            'form':UserCreationForm,
            'error': 'Passwords do not match'
        })

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'registration/signup_new.html',{
            'form':AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'registration/signin.html',{
                'form':AuthenticationForm,
                'error':'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('home')

