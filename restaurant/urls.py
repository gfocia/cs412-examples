## restaurant/urls.py
## description: the app-specific URLS for the restaurant application

from django.urls import path
from django.conf import settings
from . import views


# create a list of URLs for this app:
urlpatterns = [ 
    path('', views.main, name='main'),
    path('main/', views.main, name="main"),  
    path('order/', views.order, name="order"),  
    path('confirmation/', views.confirmation, name="confirmation"),  
    path(r'submit', views.submit, name="submit"), ## new for assignment 4
]
