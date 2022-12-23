from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class UserAccountModel(models.Model):
    name = models.CharField(max_length=50, blank=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    about_me = models.TextField(blank=True)
    dob = models.DateField()
    profile_image = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.user_name.username