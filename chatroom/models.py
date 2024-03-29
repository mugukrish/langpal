from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class ChatRoomsList(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description  = models.TextField(null=True)
    coverimage = models.ImageField(null=True)
    
    def __str__(self):
        return self.slug

class UserMessage(models.Model):
    room = models.ForeignKey(ChatRoomsList, related_name='message', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    image_message = models.ImageField(null=True)
    date_added = models.DateTimeField(default=now)

    class Meta:
        ordering = ('date_added',)
    
    def __str__(self):
        # return self.room.name
        return str(self.date_added)