# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    newer = "placeholder to display a new form to create a new blog"
    return HttpResponse(newer)

def create(request):
    return redirect('/')

def show(request):
    response = "placeholder to display blog {{number}}"
    return HttpResponse(response)

def edit(request):
    response = "placeholder to edit blog {{number}}"
    return HttpResponse(response)

def destroy(request):
    return redirect('/')