from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth.models import User

from account import views
from .models import UserPostModel, PostVoteUpdate



def check_what_vote(post_id, user_id):
    post_data = PostVoteUpdate.objects.filter(post_id=post_id, user=user_id).first()

    if post_data:
        return post_data.voted_as
    else:
        return None
    


def check_and_update_post_votes(post_id, user_id, vote_type):
    post_data = PostVoteUpdate.objects.filter(post_id=post_id, user=user_id).first()
    post_model = UserPostModel.objects.get(id=post_id)
    user_model = User.objects.get(username=user_id)

    if post_data:
        user_has_voted_for = post_data.voted_as
        if user_has_voted_for==vote_type:
            post_data.delete()

        return user_has_voted_for

    else:
        PostVoteUpdate.objects.create(post_id=post_model, user=user_model, voted_as=vote_type)
        return "first_upvote"
    




def postupvoteupdate(request, **kwargs):
    id = kwargs['pk']
    post_details = UserPostModel.objects.get(id=id)
    upvote_current = post_details.upvote_count

    if request.method == "GET":
        return HttpResponse(f"<div>{upvote_current}<div>")
    else:
        user_has_voted_for = check_and_update_post_votes(id, request.user, "up")

        if user_has_voted_for == 'first_upvote':
            upvote_current +=1
            post_details.upvote_count=upvote_current
            post_details.save()
        elif user_has_voted_for == 'up':
            upvote_current -=1
            post_details.upvote_count=upvote_current
            post_details.save()
        
        return HttpResponse(f'<div class="upvoted" >{upvote_current}<div>')



def postdownvoteupdate(request, **kwargs):
    id = kwargs['pk']
    post_details = UserPostModel.objects.get(id=id)
    downvote_current = post_details.downvote_count

    if request.method=="GET":
        return HttpResponse(f"<div>{downvote_current}<div>")
    else:
        user_has_voted_for = check_and_update_post_votes(id, request.user, "down")
        print(user_has_voted_for)
        if user_has_voted_for == 'first_upvote':
            downvote_current +=1
            post_details.downvote_count=downvote_current
            post_details.save()
        elif user_has_voted_for == 'down':
            downvote_current -=1
            post_details.downvote_count=downvote_current
            post_details.save()
        
        return HttpResponse(f"<div>{downvote_current}<div>")
    




def testhtmx(request, *args, **kwargs):
    if request.user.is_authenticated:
        current_user = request.user
        posts = UserPostModel.objects.all()
        paginator = Paginator(posts, 3)

        context = {
            'c_user':current_user,
            'post':paginator.page(kwargs['page'])
        }
        return render(request, 'homefeed/home.html', context)
    
    

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
        # paginator = Paginator(posts, 3)

        test_data = []

        for i in posts:
            data_to_append = i.__dict__
            data_to_append["vote"] = check_what_vote(i.id, request.user)
            test_data.append(data_to_append)

        paginator = Paginator(test_data, 3)

        context = {
            'c_user':current_user,
            'post':paginator.page(1),
            'data':test_data
        }
        return render(request, 'homefeed/home.html', context)
    else:
        return redirect('account_home_view')


# def homefeedview(request):
#     if request.user.is_authenticated:
#         current_user = request.user
#         posts = UserPostModel.objects.all()
#         context = {
#             'c_user':current_user,
#             'post':posts
#         }
#         return render(request, 'homefeed/home.html', context)
#     else:
#         return redirect('account_home_view')
    

def postupload(request):
    if request.method == 'POST':
        user_object = User.objects.get(username=request.user)
        post_created = UserPostModel(user_name=user_object,
                                    post_text=request.POST['user_post'])
        post_created.save()
        return redirect(homefeedview)


