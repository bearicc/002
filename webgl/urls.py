from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views


admin.site.site_header = 'Login in'

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^cube/', views.cube),
    url(r'^cube_sphere/', views.cube_sphere),
)
