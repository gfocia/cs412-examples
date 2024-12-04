from django.urls import path
from .views import (
    ShowAllProfilesView, 
    ShowProfilePageView, 
    CreateProfileView, 
    UpdateProfileView, 
    ShowAllAestheticsView, 
    ShowAestheticPageView, 
    CreateAestheticView,  # New View for creating aesthetics
    ShowAllOutfitIdeasView, 
    ShowOutfitIdeaPageView, 
    CreateOutfitIdeaView, 
    ShowAllOutfitSuggestionsView, 
    ShowOutfitSuggestionPageView, 
    CreatePostView, 
    UpdatePostView, 
    DeletePostView, 
    ShowHomePageView, 
    CreateOutfitSuggestionView,
    register_user
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Profile URLs
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'),  # Home page displaying all profiles.
    path('profiles/<int:pk>/', ShowProfilePageView.as_view(), name='show_profile'),  # View a specific profile by ID.
    path('profiles/create/', CreateProfileView.as_view(), name='create_profile'),  # Create a new profile.
    path('profiles/<int:pk>/update/', UpdateProfileView.as_view(), name='update_profile'),  # Update an existing profile.

    # Aesthetic URLs
    path('aesthetics/', ShowAllAestheticsView.as_view(), name='show_all_aesthetics'),  # View all aesthetics.
    path('aesthetics/<int:pk>/', ShowAestheticPageView.as_view(), name='show_aesthetic'),  # View a specific aesthetic by ID.

    # Outfit Idea URLs
    path('outfitideas/', ShowAllOutfitIdeasView.as_view(), name='show_all_outfitideas'),  # View all outfit ideas.
    path('outfitideas/<int:pk>/', ShowOutfitIdeaPageView.as_view(), name='show_outfitidea'),  # View a specific outfit idea by ID.
    path('outfitideas/create/', CreateOutfitIdeaView.as_view(), name='create_outfitidea'),  # Create a new outfit idea.

    # Outfit Suggestion URLs
    path('outfitsuggestions/', ShowAllOutfitSuggestionsView.as_view(), name='show_all_outfitsuggestions'),  # View all outfit suggestions.
    path('outfitsuggestions/<int:pk>/', ShowOutfitSuggestionPageView.as_view(), name='show_outfitsuggestion'),  # View a specific outfit suggestion by ID.

    # Post URLs
    path('profiles/<int:pk>/posts/create/', CreatePostView.as_view(), name='create_post'),  # Create a post associated with a profile.
    path('posts/<int:pk>/update/', UpdatePostView.as_view(), name='update_post'),  # Update an existing post by ID.
    path('posts/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),  # Delete a specific post by ID.

    # Home Page URL
    path('home/', ShowHomePageView.as_view(), name='home'),  # Newsfeed-like home page showing all posts.

    # Create Aesthetic URL
    path('aesthetics/create/', CreateAestheticView.as_view(), name='create_aesthetic'),  # Create a new aesthetic.

    # Create Outfit Suggestion URL
    path('outfitsuggestions/create/', CreateOutfitSuggestionView.as_view(), name='create_outfitsuggestion'),  # Create a new outfit suggestion.

    # Authentication URLs
    path('login/', LoginView.as_view(template_name='project/login.html'), name='login'),  # User login page.
    path('logout/', LogoutView.as_view(template_name='project/logout.html'), name='logout'),  # User logout page.

    # User Registration URL
    path('register/', register_user, name='register_user'),  # Register a new user.
]
