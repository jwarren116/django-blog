from django.conf.urls import patterns, url
from http import views

urlpatterns = patterns('',
    url(r'^$', views.http, name='http'),
)
