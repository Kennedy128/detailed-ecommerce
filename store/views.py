from django.shortcuts import render,redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse
import json
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
    return render(request,'cart.html' , context)


@login_required
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action: ',action)
    print('ProductId: ',productId)

    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order,created = Order.objects.get_or_create(customer = customer , complete = False)
    orderItem,created = OrderItem.objects.get_or_create(order = order , product = product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)



