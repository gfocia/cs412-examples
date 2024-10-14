from django.urls import reverse ## NEW for assignment 6 
from django.shortcuts import render
from . models import * 
from django.views.generic import ListView, DetailView, CreateView 
from .forms import CreateProfileForm ## NEW for assignment 6 


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

class CreateProfileView(CreateView): ## NEW for assignment 6 
    ''' A View to create a new Profile Page '''

    model = Profile 
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'
    
    def get_success_url(self) -> str:
        '''Return the URL to redirect to after successful profile creation'''
        return reverse('show_all_profiles') 

    def form_valid(self, form):
        '''This method executes after form submission if the form is valid'''
        return super().form_valid(form)
