from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^news/$', views.news, name='news and stocks'),
    url(r'^articles/$', views.articles, name='articles'),
]
