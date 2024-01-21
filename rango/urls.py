"""Reqired Modules"""
from django.urls import path, re_path
from rango import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('smart_house.html', views.smart_house, name='smart_house'),
    re_path(r'^category/(?P<category_name_slug>[\w\-]+)/$',
            views.show_category, name='show_category')
    # by naming our url mapping 'name='index' we can employ reverse url
    # matcing later on
]
