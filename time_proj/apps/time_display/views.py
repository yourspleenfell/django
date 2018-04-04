# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    context = {
        "date":strftime("%a, %B %d, %Y"),
        "time":strftime("%H:%M %p", gmtime())
    }
    return render(request, 'time_display/index.html', context)