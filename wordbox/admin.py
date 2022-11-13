from django.contrib import admin

from .models import UserMeaningHistory, GlobalMeaningModel

# Register your models here.
admin.site.register([GlobalMeaningModel, UserMeaningHistory])