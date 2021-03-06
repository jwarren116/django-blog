from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)/$', views.entry, name='entry'),
    url(r'^posts/$', views.posts, name='posts'),
)
