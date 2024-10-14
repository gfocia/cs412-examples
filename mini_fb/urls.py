from django.urls import path
from django.conf import settings
from . import views

# create a list of URLs for this app:
urlpatterns = [
    path(r'', views.ShowAllProfilesView.as_view(), name="show_all_profiles"), ## new for assignment 5 
     path(r'profile/<int:pk>/', views.ShowProfilePageView.as_view(), name="profile"), ## NEW for assignment 6 
]