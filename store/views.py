from django.shortcuts import render, redirect
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
from .models import Product, Category

def category(request,foo):
    #tirando o hifen
    foo = foo.replace("-"," ")
    #pegando a categoria da url
    try:
        #olhando para a categoria
        category =Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request,'category.html',{'products':products, 'category':category})
    except:
        messages.success(request, ("That category doesn't exist"))
        return redirect('home')

def home(request):
    products = models.Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = authenticate(request, username=username1, password=password1)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Logged In"))
            return redirect('home')
        else:
            messages.success(request, ("There Was An Error, Please Try Again"))
            return redirect('login')


    else:

        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Have Logged Out"))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            username1 = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username1, password1 = password)
            login(request, user)
            messages.success(request, ("Você foi registrado com sucesso!")) 
            return redirect('home')
        else:
            messages.success(request, ("Ocorreu um erro, tente novamente."))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form' : form})
    
def product(request,pk):
	product = Product.objects.get(id=pk)
	return render(request, 'product.html', {'product':product})

def contact(request):
    return render(request, 'contact_summary.html', {})