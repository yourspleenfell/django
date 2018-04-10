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
            errors['first_name']="First name must be greater than 2 characters"
        elif not NAME_REGEX.match(postData['first_name']):
            errors['first_name']="First name can consist of only letters"
        if len(postData['last_name']) < 2:
            errors['last_name']="Last name must be greater than 2 characters"
        elif not NAME_REGEX.match(postData['last_name']):
            errors['last_name']="Last name can consist of only letters"
        if len(postData['email']) is 0:
            errors['email']="You must enter an email address"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email']="Email must follow the standard format"
        elif User.objects.filter(email=postData['email']):
            errors['email']="Email already registered to an account"
        if len(postData['password']) < 8:
            errors['password']="Password must be at least 8 characters"
        if postData['password'] != postData['password_confirm']:
            errors['password_confirm']="Both passwords must match"
        elif not PWD_REGEX.match(postData['password']):
            errors['password']="Password must contain one capital letter and one number"
        return errors
    def login_validator(self, postData):
        errors = []
        if User.objects.filter(email=postData['email']):
            user = User.objects.filter(email=postData['email'])
            if bcrypt.checkpw(postData['password'].encode(),user[0].password.encode()):
                return user
            errors.append("Incorrect password entered")
            return errors
        else:
            errors.append("No user with that email address")
            return errors
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    objects = UserManager()