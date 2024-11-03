from django.db import models
from django.contrib.auth.models import User ## NEW for assignment 9 

# Create your models here.
class Profile(models.Model):
    ''' Encapsulates the data for a facebook Profile by some user.'''


    ## NEW for assignment 9 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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

    def get_friends(self): ## NEW for assignment 8 
        ''' Returns a list of profiles that are friends with this profile '''
        friends_as_profile1 = Friend.objects.filter(profile1=self).values_list('profile2', flat=True)
        friends_as_profile2 = Friend.objects.filter(profile2=self).values_list('profile1', flat=True)
        
        friend_ids = set(friends_as_profile1).union(set(friends_as_profile2))
        return Profile.objects.filter(id__in=friend_ids)

    def add_friend(self, other): ## NEW for assignment 8 
        '''
        Add a Friend relation between self and another Profile (other) ''' 
        if self == other:
            return

        existing_friend = Friend.objects.filter(
            models.Q(profile1=self, profile2=other) | models.Q(profile1=other, profile2=self)
        ).exists()

        if not existing_friend:
            Friend.objects.create(profile1=self, profile2=other)

    def get_friend_suggestions(self): ## NEW for assignment 8 
        ''' Return a list of possible friends for this Profile. '''

        all_profiles = Profile.objects.exclude(id=self.id)
        print(f"All Profiles (excluding self): {[profile.id for profile in all_profiles]}")


        friends = Friend.objects.filter(
            models.Q(profile1=self) | models.Q(profile2=self)
        ).values_list('profile1', 'profile2')

        friend_ids = set()
        for profile1_id, profile2_id in friends:
            if profile1_id != self.id:
                friend_ids.add(profile1_id)
            if profile2_id != self.id:
                friend_ids.add(profile2_id)

        suggestions = all_profiles.exclude(id__in=friend_ids)

        return suggestions

    def get_news_feed(self): ## NEW for assignment 8 
        ''' Return a QuerySet of StatusMessages for the profile and all their friends '''

        own_status_messages = StatusMessage.objects.filter(profile=self)
        friends = self.get_friends()
        friend_status_messages = StatusMessage.objects.filter(profile__in=friends)
        news_feed = own_status_messages.union(friend_status_messages).order_by('-timestamp')

        return news_feed

    def __str__(self):
        ''' Return a string representation of the user '''
        return f"{self.first_name} {self.last_name}"

class StatusMessage(models.Model): ## NEW for assignment 6 
    ''' Models the data attributes of a Facebook status message '''

    # data attributes
    timestamp = models.DateTimeField(auto_now_add=True)  
    message = models.TextField(blank=False) 
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) 

    def get_images(self): 
        ''' Get the images to display'''
        return Image.objects.filter(status_message=self)

    def __str__(self):
        ''' Return a string representation of the StatusMessage object '''
        return f"Status by {self.profile.first_name} {self.profile.last_name} at {self.timestamp}"

class Image(models.Model): ## NEW for assignment 7 
    ''' Models the attributes of an Image file that is stored in the Django media directory '''

    # data attributes
    image_file = models.ImageField(upload_to='')
    timestamp = models.DateTimeField(auto_now_add=True)
    status_message = models.ForeignKey(StatusMessage, on_delete=models.CASCADE)

    def __str__(self):
            ''' Return a string representation of the Image object '''
            return f"Image for {self.status_message.profile.first_name} at {self.timestamp}"

class Friend(models.Model): ## NEW for assignment 98 
    ''' Models the attributes of the mini fb Friends of a given mini fb Profile '''

    # data attributes 
    profile1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile1')
    profile2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile2')
    timestamp = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        ''' Return a string representation of the Friend object '''
        return f"{self.profile1.first_name} {self.profile1.last_name} & {self.profile2.first_name} {self.profile2.last_name}"



