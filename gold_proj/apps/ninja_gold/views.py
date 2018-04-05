# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

import random
from time import gmtime, strftime

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'log' not in request.session:
        request.session['log'] = []
    return render(request, 'ninja_gold/index.html')

def process_money(request, bldg):
    gold = 0
    time = strftime("(%B %d, %Y  %H:%M:%S %p)", gmtime())
    if bldg == 'farm':
        gold = random.randint(10, 20)
        color = 'green'
        request.session['log'].append(['You have earned ' + str(gold) + ' gold from rummaging around the farm. ' + time, color])
    if bldg == 'cave':
        gold = random.randint(5, 10)
        color = 'green'
        request.session['log'].append(['You have earned ' + str(gold) + ' gold exploring the dingy cave. ' + time, color])
    if bldg == 'house':
        gold = random.randint(2, 5)
        color = 'green'
        request.session['log'].append(['You have earned ' + str(gold) + ' gold from looting the unsuspecting house. ' + time, color])
    if bldg == 'casino':
        chance = random.randint(0, 10)
        gold = random.randint(0, 50)
        if chance % 2 != 0:
            color = 'red'
            request.session['log'].append(['You have lost ' + str(gold) + ' gold from gambling your money away. ' + time, color])
        else:
            color = 'green'
            request.session['log'].append(['You have earned ' + str(gold) + ' gold from putting your money on the line! ' + time, color])
    request.session['gold'] += gold
    return redirect('/ninja_gold')