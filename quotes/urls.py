## quotes/urls.py
## description: the app-specific URLS for the quotes application

from django.urls import path
from django.conf import settings
from . import views


# create a list of URLs for this app:
urlpatterns = [ 
    path('', views.quote, name='quote'),
    path('quote/', views.quote, name="quote"),  
    path('show_all/', views.show_all, name="show_all"),  
    path('about/', views.about, name="about"),  
]