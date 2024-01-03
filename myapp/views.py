from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    p = Product.objects.all()
    return render(request,'store.html',{'products':p})  

def cart_id(request,product_id):
    cart = request.session.session_key(id=product_id)
    if not cart:
        cart = request.session.create()
    return cart
        
    

def add_cart(request,product_id):
    p = Product.objects.get(id=product_id)
    try:
        cart = cart.objects.get(cart_id=cart_id(request))
    except cart.DoesNotExist:
        cart_id=cart_id
    return render(request,'store.html',{'products':p})  


def cart (request):
    return render(request,'cart.html')