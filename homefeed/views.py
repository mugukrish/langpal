from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

from account import views
from .models import UserPostModel

# Create your views here.


def homefeedview(request):
    if request.user.is_authenticated:
        current_user = request.user
        posts = UserPostModel.objects.all()
        print(posts[0].user_name, posts[0].post_text)
        context = {
            'c_user':current_user,
            'post':posts
        }
        return render(request, 'homefeed/home.html', context)
    

def postupload(request):
    if request.method == 'POST':
        post_created = UserPostModel(user_name=request.user,
                                    post_text=request.POST['user_post'])
        post_created.save()
        return redirect(homefeedview)
