# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime

# Create your views here.
def index(request):
    context = {
        'time': strftime("%H:%M:%S %p, %B %d %Y")
    }
    if 'list' not in request.session:
        request.session['list'] = []
    return render(request, 'session_words/index.html', context)

def submit(request):
    # if 'big' not in request.POST:
    #     big = ""
    # else:
    #     big = request.POST['big']
    # if 'color' not in request.POST:
    #     color = ""
    # else:
    #     color = request.POST['color']
    request.session['list'].append(request.POST)
    request.session.modified = True
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')