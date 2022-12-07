from django.db import models
import uuid
import datetime


# Create your models here.
class AboutIdeaPostModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_name = models.CharField(max_length=100)
    idea_text = models.TextField()

    def __str__(self):
        return self.user_name


class AboutContactPostModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_name = models.CharField(max_length=100)
    idea_text = models.TextField()

    def __str__(self):
        return self.user_name