# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class UserManager(models.Manager):              # Basic validation, untested as of yet. Does not work in shell...
    def validation(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        if postData['email_address'] == User.objects.get(email=postData['email_address']):
            errors['email_address'] = "Email address already registered"
        if not EMAIL_REGEX.match(postData['email_address']):
            errors['email_address'] = "You must enter a valid email address"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

# Commands used
# python manage.py makemigrations
# python manage.py migrate
# python manage.py shell
# >>> from apps.users_app.models import *
# >>> User.objects.create(first_name="Dylan", last_name="Arbuthnot", email_address="y@y.com", age="27")
# >>> User.objects.create(first_name="Cody", last_name="Olk", email_address="u@u.com", age="30")
# >>> User.objects.create(first_name="Maggie", last_name="May", email_address="i@i.com", age="1")
# >>> User.objects.first()
# >>> User.objects.order_by("first_name")
# >>> third = User.objects.get(id=3)
# >>> third.delete()
# >>> User.objects.create(first_name="Maggie", last_name="May", email_address="i@i.com", age="1")
# >>> User.objects.get(id=4)
# >>> fourth = User.objects.get(id=4)
# >>> fourth.last_name="Sunshine"
# >>> fourth.save()
# >>> fifth = User.objects.get(id=5)
# >>> fifth.delete()