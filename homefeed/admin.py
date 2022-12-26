from django.contrib import admin
from .models import UserPostModel, PostVoteUpdate

# Register your models here.
admin.site.register([UserPostModel, 
                    PostVoteUpdate])
