from django.shortcuts import render
from . models import * 
from django.views.generic import ListView, DetailView 


# Create your views here.
class ShowAllProfilesView(ListView):
    ''' A view to show all Profiles '''

    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'

class ShowProfilePageView(DetailView): ## NEW for assignment 6 
    ''' A View to show all Profile Pages '''

    model = Profile 
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'