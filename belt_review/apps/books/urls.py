from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.create_user),
    url(r'^books$', views.books),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^books/logout$', views.logout),
    url(r'^books/add$', views.add_book),
    url(r'^books/create$', views.create_book),
    url(r'^books/(?P<id>\d+)$', views.view_book, name="show_book"),
    url(r'^books/(?P<id>\d+)/create_review$', views.create_review),
    url(r'^users/(?P<id>\d+)$', views.show_user),
    url(r'^books/delete/review/(?P<id>\d+)$', views.delete_review),
]