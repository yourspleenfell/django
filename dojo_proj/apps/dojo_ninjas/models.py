# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    desc = models.TextField()

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas")
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)

# python manage.py makemigrations
# python manage.py migrate
# python manage.py shell
# >>> from apps.dojo_ninjas.models import *
# >>> Dojo.objects.create(name="CodingDojo Silicon Valley", city="Mountain View", state="CA")
# >>> Dojo.objects.create(name="CodingDojo Seattle", city="Seattle", state="WA")
# >>> Dojo.objects.create(name="CodingDojo New York", city="New York", state="NY")
# >>> Dojo.objects.all()
# >>> s = Dojo.objects.get(id=2)
# >>> s.save()
# >>> Ninja.objects.create(dojo_id=s, first_name="Dylan", last_name="Arbuthnot")
# >>> dylan = Ninja.objects.get(name="Dylan")
# >>> dylan.save()
# >>> dylan.dojo.name
# >>> sv = Dojo.objects.get(id=1)
# >>> sv.save()
# >>> Ninja.objects.create(dojo=sv, first_name="Mark", last_name="Wahlberg")
# >>> Dojo.objects.first().ninjas.all()
# >>> Ninja.objects.first().dojo
# >>> Dojo.objects.get(id=1).delete()
# >>> Dojo.objects.all()
# >>> Dojo.objects.get(id=2).delete()
# >>> Dojo.objects.all()
# >>> Dojo.objects.get(id=3).delete()
# >>> Dojo.objects.all()
# >>> Dojo.objects.create(name="CodingDojo Silicon Valley", city="Mountain View", state="CA")
# >>> Dojo.objects.create(name="CodingDojo Seattle", city="Seattle", state="WA")
# >>> Dojo.objects.create(name="CodingDojo New York", city="New York", state="NY")
# >>> Dojo.objects.all()
# >>> Ninja.objects.all()
# >>> sv = Dojo.objects.get(name="CodingDojo Silicon Valley")
# >>> sv.save()
# >>> sv
# >>> s = Dojo.objects.get(name="CodingDojo Seattle")
# >>> s.save()
# >>> s
# >>> Ninja.objects.create(dojo=Dojo.objects.get(id=5), first_name="Dylan", last_name="Arbuthnot")
# >>> Ninja.objects.create(dojo=Dojo.objects.get(id=6), first_name="Mark", last_name="Wahlberg")
# >>> Ninja.objects.create(dojo=Dojo.objects.get(id=4), first_name="Harry", last_name="Potter")
# >>> Ninja.objects.create(dojo=Dojo.objects.get(id=4), first_name="Devin", last_name="Arbuthnot")
# >>> Ninja.objects.create(dojo=Dojo.objects.get(id=4), first_name="John", last_name="Doe")
# >>> Ninja.objects.create(dojo=s, first_name="Patty", last_name="Smith")
# >>> Ninja.objects.create(dojo=s, first_name="Stephen", last_name="Spielberg")
# >>> ny = Dojo.objects.get(id=5)
# >>> ny.save()
# >>> ny
# >>> Ninja.objects.create(dojo=ny, first_name="Black", last_name="Rose")
# >>> Ninja.objects.create(dojo=ny, first_name="Shia", last_name="LeBeouf")
# >>> Dojo.objects.get(id=4).ninjas.all()
# >>> Dojo.objects.first().ninjas.all()
# >>> Dojo.objects.last().ninjas.all()
# >>> quit()
# python manage.py makemigrations
# python manage.py migrate
# python manage.py shell
# >>> from apps.dojo_ninjas.models import *
# >>> Dojo.objects.first().desc
# >>> quit()