from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),
url(r'^new', views.new),
url(r'^create', views.create),
url(r'^show', views.show),
url(r'^edit', views.edit),
url(r'^destroy', views.destroy)     # This line has changed!
]
