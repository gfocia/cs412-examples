from django.urls import path
from django.conf import settings
from . import views

# create a list of URLs for this app:
urlpatterns = [
    path(r'', views.ShowAllProfilesView.as_view(), name="show_all_profiles"), ## new for assignment 5 
    path(r'profile/<int:pk>/', views.ShowProfilePageView.as_view(), name="profile"), ## NEW for assignment 6 
    path(r'create_profile/', views.CreateProfileView.as_view(), name='create_profile'),  # NEW for assignment 6 
    path(r'profile/<int:pk>/create_status/', views.CreateStatusMessageView.as_view(), name='create_status'), ## NEW for assignment 6 
    path(r'profile/<int:pk>/update/', views.UpdateProfileView.as_view(), name='update_profile'), ## NEW for assignment 7
    path(r'status/<int:pk>/delete/', views.DeleteStatusMessageView.as_view(), name ='delete'), ## NEW for assignment 7
    path(r'status/<int:pk>/update/', views.UpdateStatusMessageView.as_view(), name='update'), ## NEW for assignment 7 
    path(r'profile/<int:pk>/add_friend/<int:other_pk>/', views.CreateFriendView.as_view(), name='add_friend'), ## NEW for assignment 8 
    path(r'profile/<int:pk>/friend_suggestions/', views.ShowFriendSuggestionsView.as_view(), name='friend_suggestions'), ## NEW for assignment 8 
    path(r'profile/<int:pk>/news_feed/', views.ShowNewsFeedView.as_view(), name='news_feed'), ## NEW for assignment 8 
]