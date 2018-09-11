"""Warsztaty4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from mail_box.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new', NewPerson.as_view()),
    re_path(r'^modify/(?P<id>\d+)', Modify.as_view()),
    re_path(r'^delete/(?P<id>\d+)', Delete.as_view()),
    re_path(r'^show/(?P<id>\d+)', Single.as_view()),
    path('', Basic.as_view()),
    re_path(r'^addAddress/(?P<id>\d+)$', AddAddress.as_view()),
    re_path(r'^addEmail/(?P<id>\d+)$', AddEmail.as_view()),
    re_path(r'^addPhone/(?P<id>\d+)$', AddPhone.as_view()),
    path('new_group', NewGroup.as_view()),
    path('group_list', GroupList.as_view()),
    re_path(r'^show_group/(?P<id>\d+)$', Groups.as_view()),
    re_path(r'^addMember/(?P<id>\d+)$', AddMember.as_view()),
    #path('search', Search.as_view()),
]
