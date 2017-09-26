from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^/users$', views.index),     
    url(r'^/users/new$', views.add),     
    url(r'^/users/make$', views.make),     
    url(r'^/users/update/(?P<id>\d+)$', views.update), 
    url(r'^/users/show/(?P<id>\d+)$', views.show), 
    url(r'^/users/edit/(?P<id>\d+)$', views.edit),
    url(r'^/users/delete/(?P<id>\d+)$', views.delete),
  ]