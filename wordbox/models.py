from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class GlobalMeaningModel(models.Model):
    word = models.CharField(max_length=100, primary_key=True)
    meaning = models.JSONField()

    def __str__(self):
        return self.word


class UserMeaningHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word_searched = models.JSONField()
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


