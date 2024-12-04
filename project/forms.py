from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, OutfitIdea, StatusMessage, Aesthetic, OutfitSuggestion
from django.contrib.auth.models import User


class CreateProfileForm(forms.ModelForm):
    """
    Form to create or update a Profile.

    Fields:
        - bio: TextField for user's bio.
        - profile_picture: ImageField for user's profile picture.
    """
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']


class CreateStatusMessageForm(forms.ModelForm):
    """
    Form to create or update a StatusMessage.

    Fields:
        - message: TextField for the status message content.
        - image: ImageField to attach an image to the status message.
    """
    class Meta:
        model = StatusMessage
        fields = ['message', 'image']


class CreateOutfitIdeaForm(forms.ModelForm):
    """
    Form to create an Outfit Idea.

    Fields:
        - description: TextField for the outfit idea description.
        - style_aesthetic: ForeignKey to link the outfit idea with an aesthetic.
        - image: ImageField to upload an image for the outfit idea.
    """
    class Meta:
        model = OutfitIdea
        fields = ['description', 'style_aesthetic', 'image']


class CreateOutfitSuggestionForm(forms.ModelForm):
    """
    Form to create an Outfit Suggestion.

    Fields:
        - title: CharField for the suggestion title.
        - description: TextField for the outfit suggestion description.
        - image: ImageField to upload an image representing the suggestion.
        - items: TextField to list items included in the suggestion.
        - buy_links: JSONField to map items to their purchase links.
    """
    class Meta:
        model = OutfitSuggestion
        fields = ['title', 'description', 'image', 'items', 'buy_links']


class CreateAestheticForm(forms.ModelForm):
    """
    Form to create or update an Aesthetic.

    Fields:
        - name: CharField for the name of the aesthetic.
        - description: TextField to describe the aesthetic.
        - example_image: ImageField to upload an example image representing the aesthetic.
    """
    class Meta:
        model = Aesthetic
        fields = ['name', 'description', 'example_image']


class UserProfileCreationForm(UserCreationForm):
    """
    Combined form for creating a User and an associated Profile.

    Extra Fields:
        - bio: TextField for the user's bio.
        - profile_picture: ImageField for the user's profile picture.

    Meta:
        - Uses the User model to handle user-related fields like username and password.
        - Includes default fields from UserCreationForm.Meta.
    """
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))
    profile_picture = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User  # Handles username and password fields
        fields = UserCreationForm.Meta.fields  # Default User fields

    def save(self, commit=True):
        """
        Save the User instance and create a related Profile instance.

        Args:
            commit (bool): Whether to save the instance to the database.

        Returns:
            User: The saved User instance.
        """
        user = super().save(commit=commit)
        if commit:
            Profile.objects.create(
                user=user,
                bio=self.cleaned_data.get('bio', ''),
                profile_picture=self.cleaned_data.get('profile_picture', None)
            )
        return user


class CustomUserCreationForm(UserCreationForm):
    """
    Custom form to create a new User with an email field.

    Fields:
        - username: CharField for the user's username.
        - email: EmailField for the user's email address.
        - password1: CharField for the user's password.
        - password2: CharField for confirming the user's password.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        """
        Save the User instance with the additional email field.

        Args:
            commit (bool): Whether to save the instance to the database.

        Returns:
            User: The saved User instance.
        """
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
