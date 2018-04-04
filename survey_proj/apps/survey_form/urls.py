from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^result$', views.result),
    url(r'^surveys/process$', views.submit),
    url(r'^home$', views.index)
]