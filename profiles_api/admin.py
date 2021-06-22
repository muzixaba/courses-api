from django.contrib import admin
from profiles_api import models # get all models from app
# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
