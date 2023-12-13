from django.urls import path, re_path
from rango import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('about/', views.about, name='about')
    # by naming our url mapping 'name='index' we can employ reverse url
    # matcing later on
]
