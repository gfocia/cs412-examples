from django.contrib import admin
from .models import Profile, Aesthetic, OutfitIdea, OutfitSuggestion, Friend

# Register your models here.
admin.site.register(Profile)
admin.site.register(Aesthetic)
admin.site.register(OutfitIdea)
admin.site.register(OutfitSuggestion)
admin.site.register(Friend)