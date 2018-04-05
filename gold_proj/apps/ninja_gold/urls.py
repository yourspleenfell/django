from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninja_gold$', views.index),
    url(r'^ninja_gold/process_money', views.process_money),
    url(r'^ninja_gold/farm', views.process_money, {'bldg': 'farm'}),
    url(r'^ninja_gold/cave', views.process_money, {'bldg': 'cave'}),
    url(r'^ninja_gold/house', views.process_money, {'bldg': 'house'}),
    url(r'^ninja_gold/casino', views.process_money, {'bldg': 'casino'}),
]