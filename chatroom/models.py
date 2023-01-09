from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ChatRoomsList(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description  = models.TextField(null=True)
    coverimage = models.ImageField(null=True)

class UserMessage(models.Model):
    room = models.ForeignKey(ChatRoomsList, related_name='message', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
    
    def __str__(self):
        return self.room.name
