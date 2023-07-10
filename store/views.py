from django.shortcuts import render,redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponseRedirect

# Create your views here.

@login_required(login_url='/accounts/login/')  
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer , complete = False)
        
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
        

    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0 , 'shippping':False}
        cart_items = order['get_cart_items']


    products = Product.objects.all()
    context = {'products':products ,'cart_items': cart_items}
    return render(request,'index.html' , context)

@login_required
def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer , complete = False)
        
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
       

    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0 ,'shippping':False}
        cart_items = order['get_cart_items']

    context = {'items':items , 'order':order , 'cart_items': cart_items}
    return render(request,'index.html' , context)



