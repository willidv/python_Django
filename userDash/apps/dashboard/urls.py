from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard$', views.index),
    url(r'^new$', views.new),
    url(r'^home$', views.home),
    url(r'^adminhome$', views.adminhome),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^add$', views.add),
    url(r'^message$', views.message),
    url(r'^logout$', views.logout),
    url(r'^user/(?P<id>\w+)$', views.user),
    url(r'^user_edit/(?P<id>\w+)$', views.user_edit),
    url(r'^admin_edit/(?P<id>\w+)$', views.admin_edit),
    url(r'^update/(?P<id>\w+)$', views.update),
    url(r'^follow/(?P<id>\w+)$', views.follow),
    url(r'^remove/(?P<id>\w+)$', views.remove),
]