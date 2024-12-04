from typing import Any
import random
from typing import Dict ## NEW for assignment 6 
from django.urls import reverse ## NEW for assignment 6 
from django.shortcuts import render
from . models import * 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View 
from .forms import * ## NEW for assignment 6 
from django.http import HttpResponseRedirect ## NEW for assignment 8 
from django.contrib.auth.mixins import LoginRequiredMixin ## NEW for assignment 9 
from django.contrib.auth.forms import UserCreationForm ## NEW for assignment 9 
from django.contrib.auth import login ## NEW for assignment 9 



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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context['current_profile'] = profile  
        return context

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

        user_form = UserCreationForm(self.request.POST)

        if user_form.is_valid():  
            user = user_form.save()  
            
            profile = form.save(commit=False)  
            profile.user = user  
            profile.save()  
            
            login(self.request, user)

            return HttpResponseRedirect(self.get_success_url())
        else:
            context = self.get_context_data(form=form)
            context['user_form'] = user_form 
            return self.render_to_response(context)


    def get_object(self): ## NEW for assignment 9 
        return Profile.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs): ## NEW for assignment 9 
        context = super().get_context_data(**kwargs)
        # Create an instance of the UserCreationForm and add it to the context
        context['user_form'] = UserCreationForm()
        return context

class CreateStatusMessageView(LoginRequiredMixin, CreateView):
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

    def get_login_url(self): ## NEW for assignment 9 
        return reverse('login')


class UpdateProfileView(LoginRequiredMixin, UpdateView): ## NEW for assignment 7 
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

    def get_login_url(self): ## NEW for assignment 9 
        return reverse('login')

    def get_object(self): ## NEW for assignment 9 
        return Profile.objects.get(user=self.request.user)

class DeleteStatusMessageView(LoginRequiredMixin, DeleteView): 
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

    def get_login_url(self): ## NEW for assignment 9 
        return reverse('login')
    

class UpdateStatusMessageView(LoginRequiredMixin, UpdateView): 
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

    def get_login_url(self): ## NEW for assignment 9 
        return reverse('login')

class CreateFriendView(LoginRequiredMixin, View):
    ''' A view that allows a user to add a friend '''

    def dispatch(self, request, *args, **kwargs):
        # Handle only POST requests for adding a friend
        if request.method.lower() == 'post':
            return self.post(request, *args, **kwargs)
        # If the method is not POST, return a 405 error
        return self.http_method_not_allowed(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Extract primary keys from URL
        profile_pk = kwargs.get('pk')
        other_pk = kwargs.get('other_pk')

        # Retrieve the Profile objects based on the primary keys
        profile = Profile.objects.get(pk=profile_pk)
        other_profile = Profile.objects.get(pk=other_pk)

        # Add the friend relationship between the two profiles
        profile.add_friend(other_profile)

        # Redirect to the profile page after adding the friend
        return HttpResponseRedirect(self.get_success_url(profile.pk))

    def get_success_url(self, pk):
        ''' Return the URL to redirect to after adding a friend '''
        return reverse('profile', kwargs={'pk': pk})
    
    def get_login_url(self): ## NEW for assignment 9 
        return reverse('login')


class ShowFriendSuggestionsView(LoginRequiredMixin, DetailView): ## NEW for assignment 8 
    ''' A view that allows a user to see friend suggestions '''

    model = Profile
    template_name = 'mini_fb/friend_suggestions.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context['friend_suggestions'] = profile.get_friend_suggestions()
        return context

    def get_success_url(self):
        ''' Return the URL to redirect to after successful update '''
        return reverse('profile', kwargs={'pk': self.object.profile.pk})
    
    def get_login_url(self): ## NEW for assignment 9 
        return reverse('login')

    def get_object(self): ## NEW for assignment 9 
        return Profile.objects.get(user=self.request.user)

class ShowNewsFeedView(LoginRequiredMixin, DetailView): ## NEW for assignment 8 
    ''' A view that shows the news feed for a profile '''

    model = Profile
    template_name = 'mini_fb/news_feed.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context['news_feed'] = profile.get_news_feed()
        context['current_profile'] = profile
        return context
    
    def get_login_url(self): ## NEW for assignment 9 
        return reverse('login')

    def get_object(self): ## NEW for assignment 9 
        return Profile.objects.get(user=self.request.user)

class CreatePostView(LoginRequiredMixin, CreateView):
    ''' A View to create a new Post '''
    form_class = CreateStatusMessageForm
    template_name = 'project/create_post_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        context['profile'] = profile
        return context

    def form_valid(self, form):
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        form.instance.profile = profile
        sm = form.save()

        # Handle files (if any) here, similar to the logic above

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.kwargs['pk']})
