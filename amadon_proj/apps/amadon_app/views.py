# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'total_orders' not in request.session:
        request.session['total_orders'] = 0
    if 'total_spent' not in request.session:
        request.session['total_spent'] = 0
    return render(request, 'amadon_app/index.html')

def submit(request):
    quantity = int(request.POST['quantity'])
    request.session['total_orders'] += quantity
    if request.POST['product_id'] == '1015': # t-shirt
        request.session['item'] = 'Dojo T-shirt'
        price = 19.99
        request.session['total_spent'] += (price * quantity)
    elif request.POST['product_id'] == '2087': # sweater 
        request.session['item'] = 'Dojo Sweater'
        price = 29.99
        request.session['total_spent'] += (price * quantity)      
    elif request.POST['product_id'] == '3916': # cup
        request.session['item'] = 'Dojo Cup'
        price = 4.99
        request.session['total_spent'] += (price * quantity)
    elif request.POST['product_id'] == '4521': # book
        request.session['item'] = 'Algorithm Book'
        price = 49.99
        request.session['total_spent'] += (price * quantity)
    else:
        request.session['item'] = 'Bag of Rocks'
        price = 99.99
        request.session['total_spent'] += (price * quantity)
    request.session['quantity'] = quantity
    request.session['order'] = price * quantity
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request, 'amadon_app/checkout.html')