from django.contrib import admin

# Register your models here.
from .models import * 
admin.site.register(Profile)
admin.site.register(StatusMessage) ## NEW for assignment 6 
admin.site.register(Image) ## NEW for assignment 7
admin.site.register(Friend) ## NEW for assignment 8 
