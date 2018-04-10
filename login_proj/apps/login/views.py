# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def register(request):
    return render(request, 'login/register.html')

def user(request, id):
    return render(request, 'login/user.html')

def create(request):   
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/register')
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    pwd = request.POST['password']
    pwd_hash = bcrypt.hashpw(pwd.encode(),bcrypt.gensalt())
    user = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = pwd_hash)
    request.session['user'] = user.id
    request.session['name'] = user.first_name + ' ' + user.last_name
    return redirect(reverse('users:user', kwargs={'id': request.session['user'] }))

def login(request):
    user_login = User.objects.login_validator(request.POST)
    if user_login[0] is list:
        for item in user_login:
            messages.error(request, item)
            return redirect('/')
    request.session['user'] = user_login[0].id
    request.session['name'] = user_login[0].first_name + ' ' + user_login[0].last_name
    return redirect(reverse('users:user', kwargs={'id': request.session['user'] }))

def logout(request):
    request.session.clear()
    messages.info(request, 'Thank you for visiting, see you again soon')
    return redirect('/')