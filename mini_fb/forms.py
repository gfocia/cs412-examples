from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm): 
    ''' A form to create a Mini FB Profile '''

    ''' specifying the inner class Meta that associates with each Profile'''
    class Meta: 
        model = Profile 
        fields = ['first_name', 'last_name', 'city', 'email_address', 'profile_image_url', ]