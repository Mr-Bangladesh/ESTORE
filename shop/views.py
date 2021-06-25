from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'shop/index.html')

def products(request):
    return render(request,'shop/products.html')

def productdetails(request):
    return render(request,'shop/productdetails.html')