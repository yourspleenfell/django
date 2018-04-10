# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import  Course

# Create your views here.
def index(request):
    course_list = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', course_list)

def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/courses')
    else:
        name = request.POST['name']
        desc = request.POST['desc']
        Course.objects.create(name = name, desc = desc)
        return redirect('/courses')

def confirm_destroy(request, id):
    if request.POST['confirm']:
        course = Course.objects.get(id=id)
        messages.add_message(request, messages.INFO, course.name + ' (ID: ' + id + ') has been successfully removed.')
        course.delete()
    else:
        return redirect('/courses')
    return redirect('/courses')

def destroy(request, id):
    course = {
        'id': id,
    }
    return render(request, 'courses/confirm.html', course)
