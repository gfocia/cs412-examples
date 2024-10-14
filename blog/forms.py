# blog/forms.py

from django import forms 
from .models import Comment 

# every time you create a new form for user input, you follow this process 
class CreateCommentForm(forms.ModelForm):
    ''' A form to create Comment Data '''

    class Meta: 
        ''' associate '''
        model = Comment 

        # fields = ['article', 'author', 'text', ]
        fields = ['author', 'text', ]