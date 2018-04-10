from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^create$', views.create),
    url(r'^user/(?P<id>\d+)$', views.user, name="user"),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
]