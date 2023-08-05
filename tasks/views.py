from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def cart(request):
    return render(request, 'pages/cart.html')

def cart(request):
    return render(request, 'pages/contact.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'registration/signup.html',{
            'form':UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                        password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'registration/signup.html',{
                    'form':UserCreationForm,
                    'error':'Username already exists'
                })
        return render(request, 'registration/signup.html',{
            'form':UserCreationForm,
            'error': 'Passwords do not match'
        })

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, date_completed__isnull=True)

    return render(request, 'pages/tasks.html',{
        'tasks':tasks
    })


@login_required
def create_tasks(request):

    if request.method == 'GET':
        return render(request, 'tasks/create.html',{
            'form':TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'tasks/create.html', {
                'form':TaskForm,
                'error':'Please provide valid data'
            })

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'registration/signin.html',{
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
            return redirect('tasks')

