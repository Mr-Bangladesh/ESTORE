from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'customer/login.html')

def profile(request):
    return render(request,'customer/profile.html')

def cart(request):
    return render(request,'customer/cart.html')

def checkout(request):
    return render(request,'customer/checkout.html')

def wishlist(request):
    return render(request,'customer/wishlist.html')