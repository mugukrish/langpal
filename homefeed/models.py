from django.db import models
import uuid
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()


class UserPostModel(models.Model):

    # to change filename of the uploaded post
    def content_file_name(instance, filename):
        name, file_extension = filename.rsplit('.', 1)
        file_path = f'posts/{instance.user_name}/{instance.id}+{name}.{file_extension}'
        return file_path


    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    post_text = models.TextField()
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    image_post = models.ImageField(upload_to=content_file_name, null=True)
    posted_on = models.DateField(default=datetime.datetime.now)
    upvote_count = models.IntegerField(default=0)
    downvote_count = models.IntegerField(default=0)
    

    # def __str__(self):
    #     return self.user_name


# To keep a track of post votes
class PostVoteUpdate(models.Model):
    post_id = models.ForeignKey(UserPostModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voted_as = models.CharField(max_length=5)
