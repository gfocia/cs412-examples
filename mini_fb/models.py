from django.db import models

# Create your models here.
class Profile(models.Model):
    ''' Encapsulates the data for a facebook Profile by some user.'''

    # data attributes 
    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email_address = models.TextField(blank=False)
    profile_image_url = models.URLField(blank=True)

    def get_status_messages(self): ## NEW for assignment 6 
        ''' Returns all status messages for this Profile, ordered by timestamp '''
        return StatusMessage.objects.filter(profile=self).order_by('-timestamp')

    def get_absolute_url(self): ## NEW for assignment 6 
        ''' Returns the URL to access a particular profile instance '''
        return reverse('profile', kwargs={'pk': self.pk})

    def __str__(self):
        ''' Return a string representation of the user '''
        return f"{self.first_name} by {self.last_name}"

class StatusMessage(models.Model): ## NEW for assignment 6 
    ''' Models the data attributes of a Facebook status message '''

    # data attributes
    timestamp = models.DateTimeField(auto_now_add=True)  
    message = models.TextField(blank=False) 
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) 

    def __str__(self):
        ''' Return a string representation of the StatusMessage object '''
        return f"Status by {self.profile.first_name} {self.profile.last_name} at {self.timestamp}"



