from django.db import models
from django.contrib.auth import get_user_model
import uuid
import datetime

User = get_user_model()

#model to store feedback/feature ideas that can be submitted in about page
class AboutIdeaPostModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    idea_title = models.CharField(max_length=120, null=True)
    idea_text = models.TextField()
    idea_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.idea_title
