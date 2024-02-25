"""Reqired Modules"""
from django.urls import path, re_path
from apiAI import views

urlpatterns = [
    re_path(r'^crypto_prices/$', views.crypto_prices, name='crypto_prices'),
]
