# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
    return render(request, 'random_word/index.html')

def submit(request):
    request.session['attempts'] += 1
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    context = {
        'word': ""
    }
    for val in range(14):
        context['word'] += random.choice(letter_list)
    return render(request, 'random_word/index.html', context)

def clear(request):
    request.session['attempts'] = 0
    return render(request, 'random_word/index.html')