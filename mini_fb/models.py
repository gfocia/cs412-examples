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


def __str__(self):
    ''' Return a string representation of the user '''
    return f"{self.first_name} by {self.last_name}"


