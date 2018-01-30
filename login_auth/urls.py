from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^login/$', login, {'template_name': '../templates/login_auth/login.html'}),
    url(r'^logout/$', logout, {'template_name': '../templates/login_auth/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^accounts/profile/$', views.view_profile, name='profile'),
    url(r'^accounts/profile/edit$', views.edit_profile, name='edit profile'),
]
