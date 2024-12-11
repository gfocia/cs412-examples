# File: project/models.py
# Author: Georgina Focia (gfocia@bu.edu), (12/10/2024)
# Description: The file containing all of the models for my final project 

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    """
    Represents a user profile in the fashion app.

    Attributes:
        user (ForeignKey): Links the profile to a User instance.
        bio (TextField): A short biography of the user.
        profile_picture (ImageField): An optional profile picture.
        followers (ManyToManyField): A many-to-many relationship to other profiles for following functionality.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="project_profiles",  # Avoid migration conflicts.
    )
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    followers = models.ManyToManyField("self", related_name="following", symmetrical=False, blank=True)

    def get_friends(self):
        """
        Returns a QuerySet of profiles that are friends with this profile.
        Friends are determined by the Friend model's bidirectional relationships.
        """
        friends_as_profile1 = Friend.objects.filter(profile1=self).values_list('profile2', flat=True)
        friends_as_profile2 = Friend.objects.filter(profile2=self).values_list('profile1', flat=True)
        friend_ids = set(friends_as_profile1).union(set(friends_as_profile2))
        return Profile.objects.filter(id__in=friend_ids)

    def add_friend(self, other):
        """
        Adds a Friend relationship between this profile and another.
        Prevents duplicate or self-friendship relationships.
        """
        if self == other:
            return

        existing_friend = Friend.objects.filter(
            models.Q(profile1=self, profile2=other) | models.Q(profile1=other, profile2=self)
        ).exists()

        if not existing_friend:
            Friend.objects.create(profile1=self, profile2=other)

    def get_news_feed(self):
        """
        Returns a QuerySet of OutfitIdeas created by the profile and their friends.
        Orders the feed by the most recent creations.
        """
        own_outfits = OutfitIdea.objects.filter(profile=self)
        friends = self.get_friends()
        friend_outfits = OutfitIdea.objects.filter(profile__in=friends)
        news_feed = own_outfits.union(friend_outfits).order_by('-date_created')
        return news_feed

    def __str__(self):
        """Returns the username of the associated User."""
        return self.user.username


class Aesthetic(models.Model):
    """
    Represents a style aesthetic category.

    Attributes:
        name (CharField): The name of the aesthetic.
        description (TextField): A detailed description of the aesthetic.
        example_image (ImageField): An optional image showcasing the aesthetic.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    example_image = models.ImageField(upload_to="aesthetic_examples/", blank=True, null=True)

    def __str__(self):
        """Returns the name of the aesthetic."""
        return self.name


class OutfitIdea(models.Model):
    """
    Represents outfit ideas created by users.

    Attributes:
        profile (ForeignKey): The profile that created the outfit idea.
        description (TextField): A brief description of the outfit.
        date_created (DateTimeField): The timestamp of creation.
        style_aesthetic (ForeignKey): The aesthetic style associated with the outfit.
        image (ImageField): An optional image of the outfit.
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    style_aesthetic = models.ForeignKey(Aesthetic, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="outfit_idea_images/", blank=True, null=True)

    def __str__(self):
        """Returns a string combining the user's name and the associated aesthetic."""
        return f"{self.profile.user.username}'s outfit idea ({self.style_aesthetic.name})"


class OutfitSuggestion(models.Model):
    """
    Represents a tailored outfit suggestion for a specific aesthetic.

    Attributes:
        aesthetic (ForeignKey): The aesthetic style associated with the suggestion.
        title (CharField): The title of the suggestion.
        description (TextField): A detailed description of the outfit.
        image (ImageField): An optional image of the suggestion.
        items (TextField): A list of items included in the suggestion.
        buy_links (JSONField): A dictionary mapping items to purchase links.
    """
    aesthetic = models.ForeignKey(Aesthetic, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to="outfit_suggestions/")
    items = models.TextField()
    buy_links = models.JSONField(blank=True, null=True)

    def __str__(self):
        """Returns the title of the outfit suggestion."""
        return self.title


class Friend(models.Model):
    """
    Represents a friendship between two profiles.

    Attributes:
        profile1 (ForeignKey): One of the profiles in the friendship.
        profile2 (ForeignKey): The other profile in the friendship.
        timestamp (DateTimeField): The time the friendship was created.
    """
    profile1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='friendships1')
    profile2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='friendships2')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string showing both profiles in the friendship."""
        return f"{self.profile1.user.username} & {self.profile2.user.username}"


class StatusMessage(models.Model):
    """
    Represents status messages posted by profiles.

    Attributes:
        profile (ForeignKey): The profile that posted the status.
        message (TextField): The content of the status.
        timestamp (DateTimeField): The time the status was created.
        image (ImageField): An optional image accompanying the status.
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="status_images/", blank=True, null=True)

    def __str__(self):
        """Returns a string representation of the status, including the profile name and timestamp."""
        return f"Status by {self.profile.user.username} at {self.timestamp}"
