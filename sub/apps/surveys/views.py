# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    context = {
        'value': "placeholder to display all the surveys created"
    }
    return render(request, 'surveys/index.html', context)

def new(request):
    context = {
        'value': "placeholder for users to add a new survey"
    }
    return render(request, 'surveys/index.html', context)