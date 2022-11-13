from django.db import models

# Create your models here.
class GlobalMeaningModel(models.Model):
    word = models.CharField(max_length=100, primary_key=True)
    meaning = models.JSONField()

    def __str__(self):
        return self.word
