# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'books/index.html')

def create_user(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            print error
            messages.error(request, error, extra_tags=tag)
            return redirect('/')
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    alias = request.POST['alias']
    email = request.POST['email']
    password = request.POST['password']
    pwd_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
    user = User.objects.create(first_name = first_name, last_name = last_name, alias = alias, email = email, password = pwd_hash)
    request.session['id'] =  user.id
    request.session['name'] = user.first_name + ' ' + user.last_name
    return redirect('/books')

def books(request):
    books_review = {
        'books': Book.objects.all(),
        'reviews': Review.objects.all().order_by('-created_at')[:3],
    }
    return render(request, 'books/dashboard.html', books_review)

def login(request):
    user_login = User.objects.login_validator(request.POST)
    try:
        if user_login['login']:
            for tag, item in user_login.iteritems():
                print tag
                messages.error(request, item, extra_tags=tag)
                return redirect('/')
    except:
        request.session['id'] = user_login.id
        request.session['name'] = user_login.first_name + ' ' + user_login.last_name
        return redirect('/books')

def logout(request):
    messages.info(request, 'Thank you for visiting, ' + request.session['name'] + ', see you again soon')
    request.session.clear()
    return redirect('/')

def add_book(request):
    authors = {
        'authors': Author.objects.all().order_by('last_name')
    }
    return render(request, 'books/add_book.html', authors)

def create_book(request):
    print request.POST
    errors = Book.objects.validator(request.POST)
    if errors:
        for tag, item in errors.iteritems():
            messages.error(request, item, extra_tags='login')
            return redirect('/books/add')
    else:
        user_id = request.session['id']
        title = request.POST['title']
        review_content = request.POST['review']
        rating = int(request.POST['rating'])
        if len(request.POST['author']) > 0:
            author = Author.objects.get(id = request.POST['author'])
            book = Book.objects.create(title = title, author = author)
            Review.objects.create(content = review_content, rating = rating, book = book, user = User.objects.get(id=user_id))
            return redirect(reverse('book:show_book', kwargs={'id': book.id }))
        else:
            author_first_name = request.POST['first_name']
            author_last_name = request.POST['last_name']
            author = Author.objects.create(first_name = author_first_name, last_name = author_last_name)
            book = Book.objects.create(title = title, author = author)
            Review.objects.create(content = review_content, rating = rating, book = book, user = User.objects.get(id=user_id))
            return redirect(reverse('book:show_book', kwargs={'id': book.id }))

def view_book(request, id):
    book = {
        'book': Book.objects.get(id = id),
        'reviews': Review.objects.filter(book = id),
    }
    return render(request, 'books/book.html', book)

def create_review(request, id):
    review_content = request.POST['review']
    rating = request.POST['rating']
    book = Book.objects.get(id = id)
    user_id = request.session['id']
    book_review = Review.objects.create(content = review_content, rating = rating, book = book, user = User.objects.get(id=user_id))
    return redirect(reverse('book:show_book', kwargs={'id': id }))

def show_user(request, id):
    user_info = {
        'user': User.objects.get(id = id),
        'total_reviews': User.objects.get(id = id).user_reviews.count(),
        'reviewed_books': Review.objects.filter(user = id),
    }
    return render(request, 'books/user.html', user_info)

def delete_review(request, id):
    title = Review.objects.get(id = id).book.title
    messages.success(request,'Successfully deleted review for ' + title)
    Review.objects.get(id = id).delete()
    return redirect('/books')