from django.urls import path
from django.conf import settings
from . import views

# create a list of URLs for this app:
urlpatterns = [
    path(r'', views.ShowAllView.as_view(), name="show_all"), ## new for 10/1 example 
]