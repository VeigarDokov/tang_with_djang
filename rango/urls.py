from django.urls import path, re_path
from rango import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('smart_house.html', views.smart_house, name='smart_house')
    # by naming our url mapping 'name='index' we can employ reverse url
    # matcing later on
]
