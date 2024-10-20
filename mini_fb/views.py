from typing import Any
import random
from typing import Dict ## NEW for assignment 6 
from django.urls import reverse ## NEW for assignment 6 
from django.shortcuts import render
from . models import * 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
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
        ''' Attach the Profile to the StatusMessage and handle the image files before saving '''
        profile = Profile.objects.get(pk=self.kwargs['pk'])  
        form.instance.profile = profile  # Attach the Profile to the StatusMessage
            
        # Save the form, which stores the StatusMessage and returns the new object
        sm = form.save()

        # Read the file(s) from the form
        files = self.request.FILES.getlist('files')

        # Iterate through each file and create an Image object
        for file in files:
            image = Image(status_message=sm, image_file=file)  # Associate the image with the status message
            image.save()  # Save each image to the database

        return super().form_valid(form)

    def get_success_url(self):
        ''' Redirect to the profile page after successfully creating a StatusMessage '''
        return reverse('profile', kwargs={'pk': self.kwargs['pk']})

class UpdateProfileView(UpdateView): ## NEW for assignment 7 
    ''' A view to update a given Profile '''
    model = Profile 
    form_class = UpdateProfileForm 
    template_name = 'mini_fb/update_profile_form.html'

    def get_success_url(self) -> str:
        '''Return the URL to redirect to after successful profile creation'''
        return reverse('profile', kwargs={'pk': self.object.pk}) 

    def form_valid(self, form):
        '''This method executes after form submission if the form is valid'''
        return super().form_valid(form)

class DeleteStatusMessageView(DeleteView): 
    ''' A view that allows the user to delete a status messages '''
    model = StatusMessage 
    template_name = 'mini_fb/delete_status_form.html'
    context_object_name = 'status_message'

    def get_context_data(self, **kwargs):
        ''' Add the Profile to the context data for the template '''
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.object.profile.pk)
        context['profile'] = profile
        return context

    def get_success_url(self):
        ''' Return the URL to redirect to after successful deletion '''
        return reverse('profile', kwargs={'pk': self.object.profile.pk})

class UpdateStatusMessageView(UpdateView): 
    ''' A view that allows the user to update a status message '''
    model = StatusMessage
    form_class = CreateStatusMessageForm 
    template_name = 'mini_fb/update_status_form.html'
    context_object_name = 'status_message'

    def get_context_data(self, **kwargs):
        ''' Add the Profile to the context data for the template '''
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.object.profile.pk)  # Get the profile from the StatusMessage
        context['profile'] = profile
        return context

    def get_success_url(self):
        ''' Return the URL to redirect to after successful update '''
        return reverse('profile', kwargs={'pk': self.object.profile.pk})