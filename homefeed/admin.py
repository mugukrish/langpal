from django.contrib import admin
from .models import UserPostModel
from wordbox.models import GlobalMeaningModel

# Register your models here.
admin.site.register([UserPostModel, GlobalMeaningModel])
