# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
        url(r'^$',views.home, name='home'),
        url(r'^about-me/',views.about, name='about'),
        url(r'^contact/',views.contact, name='contact')
        # path('',views.home, name='home')
]
