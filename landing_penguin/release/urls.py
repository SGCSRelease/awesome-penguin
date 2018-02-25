from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = 'release'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('recruiting', views.recruiting, name='recruiting'),
]
