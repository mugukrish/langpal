from django.db import models
import uuid
import datetime


# Create your models here.
class UserPostModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    post_text = models.TextField()
    user_name = models.CharField(max_length=100)
    posted_on = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.user_name