from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

#stores the searched meaning in DB
class GlobalMeaningModel(models.Model):
    word = models.CharField(max_length=100, primary_key=True)
    meaning = models.JSONField()

    def __str__(self):
        return self.word

#stores users meaning search history
class UserMeaningHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word_searched = models.JSONField()
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

#stores sentence from searched meanings--> used for read practice app
class MeaningSentences(models.Model):
    word = models.CharField(max_length=100)
    sentence = models.TextField(null=False)


