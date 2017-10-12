from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^pbelt/register$', views.register),
    url(r'^pbelt/login$', views.login),
    url(r'^pbelt/logout$', views.logout),
    url(r'^pbelt/quote$', views.quote),
    url(r'^favorite/(?P<id>\w+)$', views.favorite),
    url(r'^pbelt/remove/(?P<id>\w+)$', views.remove),
    url(r'^user/(?P<id>\w+)$', views.user),
    # url(r'^pbelt/user/(?P<id>\w+)$', views.user),
    url(r'^home$', views.home),
    # url(r'^pbelt/home$', views.home),
]