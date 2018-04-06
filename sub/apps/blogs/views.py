# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string

def index(request):
    context = {
        'value': "placeholder to later display all the list of blogs"
    }
    return render(request, 'blogs/index.html', context)

def new(request):
    newer = "placeholder to display a new form to create a new blog"
    return HttpResponse(newer)

def create(request):
	if request.method == "POST":
		print "*"*50
		print request.POST
		print "*"*50
		return redirect("/blogs")
	else:
		return redirect("/blogs")

def show(request, num):
    response = "placeholder to display blog " + num
    return HttpResponse(response)

def edit(request, num):
    response = "placeholder to edit blog " + num
    return HttpResponse(response)

def destroy(request, num):
    return redirect('/blogs')