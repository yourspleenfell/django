# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    uploader = models.ForeignKey(User, related_name="uploaded_books")
    liked_users = models.ManyToManyField(User, related_name="liked_books")

# >>> from apps.books_likes.models import *
# >>> User.objects.create(first_name="Dylan", last_name="Arbuthnot", email="q@q.com")
# >>> user_1 = User.objects.get(id=1)
# >>> User.objects.create(first_name="Cody", last_name="Olk", email="w@w.com")
# >>> user_2 = User.objects.get(id=2)
# >>> User.objects.create(first_name="Maggie", last_name="May", email="e@e.com")
# >>> user_3 = User.objects.get(id=3)
# >>> Book.objects.create(name="The Way of Kings", desc="Epic tale across alien lands.", uploader=user_1)
# >>> Book.objects.create(name="The Name of the Wind", desc="Follow the legendary Kvothe Kingslayer as he learns about magic.", uploader=user_1)
# >>> Book.objects.create(name="Farenheit 451", desc="Books have been outlawed and destroyed. Firemen destroy any remaining.", uploader=user_2)
# >>> Book.objects.create(name="Life Expectancy", desc="Follow the pivotal moments of self-proclaimed lummox, Jimmy Tock.", uploader=user_2)
# >>> Book.objects.create(name="The Goldfinch", desc="Theo Decker recounts the story of his life.", uploader=user_3)
# >>> Book.objects.create(name="Great Expectations", desc="A classic tale about Pip on his journey through life.", uploader=user_3)
# >>> user_1.liked_books.add(Book.objects.first(), Book.objects.last())
# >>> user_2.liked_books.add(Book.objects.first(), Book.objects.get(id=3))
# >>> user_3.liked_books.add(Book.objects.first(), Book.objects.get(id=2), Book.objects.get(id=3), Book.objects.get(id=4), Book.objects.get(id=5), Book.objects.last())
# >>> Book.objects.first().liked_users.all()
# >>> Book.objects.first().uploader
# >>> Book.objects.get(id=2).liked_users.all()
# >>> Book.objects.get(id=2).uploader
# >>> user_1.save()
# >>> user_2.save()
# >>> user_3.save()
# >>> book_1=Book.objects.first()
# >>> book_2=Book.objects.get(id=2)
# >>> book_3=Book.objects.get(id=3)
# >>> book_4=Book.objects.get(id=4)
# >>> book_5=Book.objects.get(id=5)
# >>> book_6=Book.objects.last()
# >>> book_1.save()
# >>> book_2.save()
# >>> book_3.save()
# >>> book_4.save()
# >>> book_5.save()
# >>> book_6.save()
# >>> quit()