from django.contrib import admin

from .models import UserMeaningHistory, GlobalMeaningModel, MeaningSentences

# Register your models here.
admin.site.register([GlobalMeaningModel, UserMeaningHistory, MeaningSentences])