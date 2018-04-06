# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def register(request):
    context = {
        'value': "placeholder for users to create a new user record"
    }
    return render(request, 'users/index.html', context)

def login(request):
    context = {
        'value': "placeholder for users to login"
    }
    return render(request, 'users/index.html', context)

def display(request):
    context = {
        'value': "placeholder to later display all the list of users"
    }
    return render(request, 'users/index.html', context)