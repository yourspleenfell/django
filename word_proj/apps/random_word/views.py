# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
    return render(request, 'random_word/index.html')

def submit(request):
    request.session['attempts'] += 1
    context = {
        'word': get_random_string(length=14)
    }
    return render(request, 'random_word/index.html', context)

def clear(request):
    request.session['attempts'] = 0
    return render(request, 'random_word/index.html')