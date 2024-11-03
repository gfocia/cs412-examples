from django.urls import path
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views ## NEW for assignment 9 

# create a list of URLs for this app:
urlpatterns = [
    path(r'', views.ShowAllProfilesView.as_view(), name="show_all_profiles"), ## new for assignment 5 
    path(r'profile/<int:pk>/', views.ShowProfilePageView.as_view(), name="profile"), ## NEW for assignment 6 
    path(r'create_profile/', views.CreateProfileView.as_view(), name='create_profile'),  # NEW for assignment 6 
    path(r'status/create_status/', views.CreateStatusMessageView.as_view(), name='create_status'), ## NEW for assignment 6 
    path(r'profile/update/', views.UpdateProfileView.as_view(), name='update_profile'), ## NEW for assignment 7
    path(r'status/<int:pk>/delete/', views.DeleteStatusMessageView.as_view(), name ='delete'), ## NEW for assignment 7
    path(r'status/<int:pk>/update/', views.UpdateStatusMessageView.as_view(), name='update'), ## NEW for assignment 7 
    path(r'profile/add_friend/<int:other_pk>/', views.CreateFriendView.as_view(), name='add_friend'), ## NEW for assignment 8 
    path(r'profile/friend_suggestions/', views.ShowFriendSuggestionsView.as_view(), name='friend_suggestions'), ## NEW for assignment 8 
    path(r'profile/news_feed/', views.ShowNewsFeedView.as_view(), name='news_feed'), ## NEW for assignment 8 
    # authentication urls 
    path('login/', auth_views.LoginView.as_view(template_name="mini_fb/login.html"), name='login'), ## NEW for assignment 9  
    path('logout/', auth_views.LogoutView.as_view(template_name='mini_fb/logged_out.html'), name="logout"), ## NEW for assignment 9 
]