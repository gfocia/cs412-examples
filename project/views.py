from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin  # Import for requiring login
from .models import Profile, Aesthetic, OutfitIdea, OutfitSuggestion, Friend, StatusMessage
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import (
    CreateProfileForm,
    CreateStatusMessageForm,
    CreateOutfitIdeaForm,
    CreateOutfitSuggestionForm,
    CreateAestheticForm, 
    CustomUserCreationForm
)


# Profile Views
class ShowAllProfilesView(ListView):
    """
    Display a list of all profiles on the website.
    Template: project/show_all_profiles.html
    """
    model = Profile
    template_name = 'project/show_all_profiles.html'
    context_object_name = 'profiles'


class ShowProfilePageView(DetailView):
    """
    Display details of a specific profile.
    Template: project/show_profile.html
    """
    model = Profile
    template_name = 'project/show_profile.html'
    context_object_name = 'profile'


class CreateProfileView(CreateView):
    """
    Allow users to create a new profile.
    Template: project/create_profile_form.html
    """
    model = Profile
    template_name = 'project/create_profile_form.html'
    fields = ['user', 'bio', 'profile_picture']

    def get_success_url(self):
        """
        Redirect to the profiles page after successful creation.
        """
        return reverse('show_all_profiles')


class UpdateProfileView(UpdateView):
    """
    Allow users to update their profile information.
    Template: project/update_profile_form.html
    """
    model = Profile
    template_name = 'project/update_profile_form.html'
    fields = ['bio', 'profile_picture']

    def get_success_url(self):
        """
        Redirect to the profile detail page after updating.
        """
        return reverse('show_profile', kwargs={'pk': self.object.pk})


# Aesthetic Views
class ShowAllAestheticsView(ListView):
    """
    Display a list of all aesthetics.
    Template: project/show_all_aesthetics.html
    """
    model = Aesthetic
    template_name = 'project/show_all_aesthetics.html'
    context_object_name = 'aesthetics'


class ShowAestheticPageView(DetailView):
    """
    Display details of a specific aesthetic.
    Template: project/show_aesthetic.html
    """
    model = Aesthetic
    template_name = 'project/show_aesthetic.html'
    context_object_name = 'aesthetic'


# Outfit Idea Views
class ShowAllOutfitIdeasView(ListView):
    """
    Display a list of all outfit ideas.
    Template: project/show_all_outfitideas.html
    """
    model = OutfitIdea
    template_name = 'project/show_all_outfitideas.html'
    context_object_name = 'outfitideas'


class ShowOutfitIdeaPageView(DetailView):
    """
    Display details of a specific outfit idea.
    Template: project/show_outfitidea.html
    """
    model = OutfitIdea
    template_name = 'project/show_outfitidea.html'
    context_object_name = 'outfitidea'


class CreateOutfitIdeaView(LoginRequiredMixin, CreateView):
    """
    Allow logged-in users to create a new outfit idea.
    Template: project/create_outfitidea_form.html
    """
    model = OutfitIdea
    form_class = CreateOutfitIdeaForm
    template_name = 'project/create_outfitidea_form.html'

    def form_valid(self, form):
        """
        Associate the outfit idea with the logged-in user's profile.
        """
        form.instance.profile = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirect to the outfit ideas page after creation.
        """
        return reverse('show_all_outfitideas')


# Outfit Suggestion Views
class ShowAllOutfitSuggestionsView(ListView):
    """
    Display a list of all outfit suggestions.
    Template: project/show_all_outfitsuggestions.html
    """
    model = OutfitSuggestion
    template_name = 'project/show_all_outfitsuggestions.html'
    context_object_name = 'outfitsuggestions'


class ShowOutfitSuggestionPageView(DetailView):
    """
    Display details of a specific outfit suggestion.
    Template: project/show_outfitsuggestion.html
    """
    model = OutfitSuggestion
    template_name = 'project/show_outfitsuggestion.html'
    context_object_name = 'outfitsuggestion'


class CreateOutfitSuggestionView(LoginRequiredMixin, CreateView):
    """
    Allow logged-in users to create a new outfit suggestion.
    Template: project/create_outfitsuggestion_form.html
    """
    model = OutfitSuggestion
    template_name = 'project/create_outfitsuggestion_form.html'
    fields = ['aesthetic', 'title', 'description', 'image', 'items', 'buy_links']

    def get_success_url(self):
        """
        Redirect to the outfit suggestions page after creation.
        """
        return reverse('show_all_outfitsuggestions')


class UpdatePostView(LoginRequiredMixin, UpdateView):
    """
    Allow logged-in users to update a status message.
    Template: project/update_post_form.html
    """
    model = StatusMessage
    form_class = CreateStatusMessageForm
    template_name = 'project/update_post_form.html'

    def get_success_url(self):
        """
        Redirect to the associated profile's page after updating.
        """
        return reverse('show_profile', kwargs={'pk': self.object.profile.pk})


class DeletePostView(LoginRequiredMixin, DeleteView):
    """
    Allow logged-in users to delete a status message.
    Template: project/delete_post_form.html
    """
    model = StatusMessage
    template_name = 'project/delete_post_form.html'

    def get_success_url(self):
        """
        Redirect to the associated profile's page after deletion.
        """
        return reverse('show_profile', kwargs={'pk': self.object.profile.pk})


class CreatePostView(LoginRequiredMixin, CreateView):
    """
    Allow logged-in users to create a new status message.
    Template: project/create_post_form.html
    """
    form_class = CreateStatusMessageForm
    template_name = 'project/create_post_form.html'

    def get_context_data(self, **kwargs):
        """
        Add the associated profile to the context.
        """
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        context['profile'] = profile
        return context

    def form_valid(self, form):
        """
        Associate the status message with a profile.
        """
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        form.instance.profile = profile
        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirect to the associated profile's page after creation.
        """
        return reverse('show_profile', kwargs={'pk': self.kwargs['pk']})


class ShowHomePageView(LoginRequiredMixin, ListView):
    """
    Display a feed of all status messages on the homepage.
    Template: project/home.html
    """
    model = StatusMessage
    template_name = 'project/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """
        Order the status messages by most recent.
        """
        return StatusMessage.objects.order_by('-timestamp')


class CreateAestheticView(LoginRequiredMixin, CreateView):
    """
    Allow logged-in users to create a new aesthetic.
    Template: project/create_aesthetic_form.html
    """
    model = Aesthetic
    form_class = CreateAestheticForm
    template_name = 'project/create_aesthetic_form.html'

    def get_success_url(self):
        """
        Redirect to the aesthetics page after creation.
        """
        return reverse('show_all_aesthetics')


def register_user(request):
    """
    Handle user registration and automatically log them in after creation.
    Template: project/register.html
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('show_all_profiles')
    else:
        form = CustomUserCreationForm()
    return render(request, 'project/register.html', {'form': form})
