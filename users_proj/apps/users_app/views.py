# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import *

# Create your views here.
def index(request):
    user_list = {
        'users': User.objects.all(),
    }
    return render(request, 'users_app/index.html', user_list)

def new(request):
    return render(request, 'users_app/new.html')

def show(request, id):
    current_user = {
        'user': User.objects.get(id=id),
    }
    return render(request, 'users_app/dashboard.html', current_user)

def edit(request, id):
    current_user = {
        'user': User.objects.get(id=id),
    }
    return render(request, 'users_app/edit.html', current_user)

def create(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email_address']
    age = request.POST['age']
    User.objects.create(first_name = first_name, last_name = last_name, email_address = email, age = age)
    return redirect('/users')

def destroy(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/users')

def update(request, id):
    user = User.objects.get(id=id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email_address = request.POST['email_address']
    user.age = request.POST['age']
    user.save()
    return redirect(reverse('users:show', kwargs={'id': id }))