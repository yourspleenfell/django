# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string

def index(request):
    context = {
        'email': 'blog@gmail.com',
        'name': 'mike'
    }
    # response = "placeholder to later display all the list of blogs"
    return render(request, 'blogs/index.html', context)

def new(request):
    newer = "placeholder to display a new form to create a new blog"
    return HttpResponse(newer)

def create(request):
	if request.method == "POST":
		print "*"*50
		print request.POST
		print "*"*50
		return redirect("/")
	else:
		return redirect("/")

def show(number):
    response = "placeholder to display blog {{number}}"
    return HttpResponse(response)

def edit(request, edit):
    number = request
    print number
    response = "placeholder to edit blog {{request}}"
    return HttpResponse(response)

def destroy(request, delete):
    return redirect('/')