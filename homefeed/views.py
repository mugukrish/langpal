from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

from account import views
from .models import UserPostModel

# Create your views here.
def temptestview(request):
    context = {
        'object': request.user.is_authenticated
    }
    return render(request, 'base.html', context)


def homefeedview(request):
    if request.user.is_authenticated:
        current_user = request.user
        posts = UserPostModel.objects.all()
        context = {
            'c_user':current_user,
            'post':posts
        }
        return render(request, 'homefeed/home.html', context)
    else:
        return redirect('account_home_view')
    

def postupload(request):
    if request.method == 'POST':
        post_created = UserPostModel(user_name=request.user,
                                    post_text=request.POST['user_post'])
        post_created.save()
        return redirect(homefeedview)
