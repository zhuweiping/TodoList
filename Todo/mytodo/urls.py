"""Todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
import views as todo_views
urlpatterns = [
    url(r'^$',todo_views.todolists),
    url(r'^newfinishedtodo/(?P<id>\d+)/$',todo_views.newfinishedtodo,name='finished'),
    url(r'^rebacktodo/(?P<id>\d+)/$',todo_views.rebacktodo,name='reback'),
    url(r'^addtodo/$',todo_views.addtodo,name='add'),
    url(r'^deltodo/(?P<id>\d+)/$',todo_views.deltodo,name='del'),
    url(r'^update/(?P<id>\d+)/$',todo_views.updatetodo,name='update'),

]
