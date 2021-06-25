from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name="login"),
    path('profile',views.profile,name="profile"),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name="checkout"),
    path('wishlist',views.wishlist,name="wishlist"),
    path('login',views.login,name="login"),
]
