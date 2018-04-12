# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PWD_REGEX = re.compile(r'(?=.*[A-Z])(?=.*[0-9])')

# Create your models here.
class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['register']="First name must be greater than 2 characters"
        elif not NAME_REGEX.match(postData['first_name']):
            errors['register']="First name can consist of only letters"
        if len(postData['last_name']) < 2:
            errors['register']="Last name must be greater than 2 characters"
        elif not NAME_REGEX.match(postData['last_name']):
            errors['register']="Last name can consist of only letters"
        if len(postData['email']) is 0:
            errors['register']="You must enter an email address"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['register']="Email must follow the standard format"
        elif User.objects.filter(email=postData['email']):
            errors['register']="Email already registered to an account"
        if len(postData['password']) < 8:
            errors['register']="Password must be at least 8 characters"
        if postData['password'] != postData['password_con']:
            errors['register']="Both passwords must match"
        elif not PWD_REGEX.match(postData['password']):
            errors['register']="Password must contain one capital letter and one number"
        return errors
    def login_validator(self, postData):
        errors = {}
        if len(postData['email']) is 0:
            errors['login'] = "Must enter an email address to login"
            return errors
        if User.objects.filter(email=postData['email']):
            user = User.objects.filter(email=postData['email'])
            if bcrypt.checkpw(postData['password'].encode(),user[0].password.encode()):
                user = User.objects.get(email=postData['email'])
                return user
            else:
                errors['login'] = "Incorrect password entered"
                return errors
        else:
            errors['login'] = "No user with that email address"
            return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class BookManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title']) is 0:
            errors['title'] = "You must a book title"
        try:
            author_id = postData['author']
            if Author.objects.get(id = author_id):
                print author_id
        except:
            if len(postData['first_name']) is 0:
                errors['first__name'] = "Author must have a first name"
            elif len(postData['last_name']) is 0:
                errors['last_name'] = "Author must have a last name"
        if len(postData['review']) is 0:
            errors['review'] = "You must enter a review"
        return errors

class Book(models.Model):
    title = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(Author, related_name="books")
    objects=BookManager()

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    book = models.ForeignKey(Book, related_name="book_reviews")
    user = models.ForeignKey(User, related_name="user_reviews")