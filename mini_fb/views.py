from typing import Any
import random
from typing import Dict ## NEW for assignment 6 
from django.urls import reverse ## NEW for assignment 6 
from django.shortcuts import render
from . models import * 
from django.views.generic import ListView, DetailView, CreateView 
from .forms import * ## NEW for assignment 6 


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

class CreateStatusMessageView(CreateView):
    ''' A View to create a new Status Message under a given Profile '''

    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/create_status_form.html'

    def get_context_data(self, **kwargs):
        ''' Add the Profile to the context data for the template '''
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.kwargs['pk']) 
        context['profile'] = profile  
        return context

    def form_valid(self, form):
        ''' Attach the Profile to the StatusMessage before saving '''
        profile = Profile.objects.get(pk=self.kwargs['pk'])  
        form.instance.profile = profile 
        return super().form_valid(form) 

    def get_success_url(self):
        ''' Redirect to the profile page after successfully creating a StatusMessage '''
        return reverse('profile', kwargs={'pk': self.kwargs['pk']})
