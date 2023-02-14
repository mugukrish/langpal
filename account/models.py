from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Model to store extra data of the registered users
class UserAccountModel(models.Model):

    #below function will change the image name before saving
    def content_file_name(instance, filename):
        name, ext = filename.rsplit('.', 1)
        file_path = f'profileimg/{instance.user_name}/{instance.id}+{name}.{ext}'
        return file_path

    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    about_me = models.TextField(blank=True)
    age = models.IntegerField()
    profile_image = models.ImageField(upload_to=content_file_name, default='blank-profile-picture.png')
    location = models.CharField(max_length=50,blank=True)


    def __str__(self):
        return self.user_name.username