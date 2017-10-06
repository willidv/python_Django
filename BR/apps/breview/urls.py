from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^new$', views.new),
    url(r'^home$', views.home),
    url(r'^add$', views.add),
    url(r'^book/(?P<id>\d+)$', views.info),
    url(r'^user/(?P<alias>\w+)$', views.user),
    url(r'^logout$', views.logout),
    url(r'^remove/(?P<id>\d+)$', views.remove),
]