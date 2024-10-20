from django import forms
from .models import Profile, StatusMessage, Image

class CreateProfileForm(forms.ModelForm): ## NEW for assignment 6 
    ''' A form to create a Mini FB Profile '''

    ''' specifying the inner class Meta that associates with each Profile'''
    class Meta: 
        model = Profile 
        fields = ['first_name', 'last_name', 'city', 'email_address', 'profile_image_url', ]


class CreateStatusMessageForm(forms.ModelForm): ## NEW for assignment 6 
    ''' A form to create a Status Message under a given Profile '''

    ''' specifying the inner class Meta that associates with each Profile '''
    class Meta: 
        model = StatusMessage 
        fields = ['message', ] ## profile and timestamp are automatically included 

class UpdateProfileForm(forms.ModelForm): ## NEW for assignment 7 
    ''' A form that allows users to modify their Profile (not including first and last name)'''

    ''' specifying the inner class Meta that is associated with each Profile '''
    class Meta:
        model = Profile
        fields = ['city', 'email_address', 'profile_image_url']