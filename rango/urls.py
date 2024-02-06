"""Reqired Modules"""
from django.urls import path, re_path
from rango import views

urlpatterns = [
    # re_path(r'^$', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('smart_house.html', views.smart_house, name='smart_house'),
    re_path(r'^category/(?P<category_name_slug>[\w\-]+)/$',
            views.show_category, name='show_category'),
    # by naming our url mapping 'name='index' we can employ reverse url
    # matcing later on
    re_path(r'^add_category/$', views.add_category, name='add_category'),
    re_path(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',
            views.add_page, name='add_page'),
    re_path(r'^contact_form/$', views.contact, name='contact_form'),
    re_path(r'^contact_sucess/$', views.contact_sucess, name='contact_sucess'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^login/$', views.user_login, name='login'),
    re_path(r'^restricted/$', views.restricted, name='restricted'),
    re_path(r'^logout/$', views.user_logout, name='logout'),
]
