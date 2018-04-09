# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    books = models.ManyToManyField(Book, related_name="authors")

# python manage.py makemigrations
# python manage.py migrate
# python manage.py shell
# >>> from apps.book_authors.models import *
# >>> Book.objects.create(name="C sharp", desc="C sharp")
# >>> Book.objects.create(name="Java", desc="Java")
# >>> Book.objects.create(name="Python", desc="Python")
# >>> Book.objects.create(name="PHP", desc="PHP")
# >>> Book.objects.create(name="Ruby", desc="Ruby")
# >>> Book.objects.all()
# >>> Author.objects.create(first_name="Mike", last_name="Smith", email="y@y.com")
# >>> Author.objects.create(first_name="Speros", last_name="Doe", email="q@q.com")
# >>> Author.objects.create(first_name="John", last_name="Jacob", email="w@w.com")
# >>> Author.objects.create(first_name="Jadee", last_name="Williams", email="e@e.com")
# >>> Author.objects.create(first_name="Jay", last_name="Johnson", email="r@r.com")
# >>> Author.objects.all()
# >>> book_5 = Book.objects.get(id=5)
# >>> book_5.save()
# >>> book_5.name="C#"
# >>> book_5.save()
# >>> auth_5 = Author.objects.get(id=5)
# >>> auth_5.first_name="Ketul"
# >>> auth_5.save()
# >>> auth_1 = Author.objects.get(id=1)
# >>> auth_1.save()
# >>> book_1 = Book.objects.get(id=1)
# >>> book_2 = Book.objects.get(id=2)
# >>> book_1 = Book.objects.get(id=1)
# >>> book_2 = Book.objects.get(id=2)
# >>> auth_2 = Author.objects.get(id=2)
# >>> auth_3 = Author.objects.get(id=3)
# >>> auth_4 = Author.objects.get(id=4)
# >>> book_1.authors.add(auth_1)
# >>> book_2.authors.add(auth_2)
# >>> auth_2.books.add(book_1, book_2, book_3)
# >>> auth_3.books.add(book_1, book_2, book_3, book_4)
# >>> auth_4.books.add(book_1, book_2, book_3, book_4, book_5)
# >>> book_3.authors
# >>> book_3.authors.first()
# >>> book_2.authors.add(auth_5)
# >>> auth_3.books.all()
# >>> auth_2.books.all()