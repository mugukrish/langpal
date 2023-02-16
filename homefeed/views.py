from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

import os

from .models import UserPostModel, PostVoteUpdate

from account.models import UserAccountModel


#check what vote the user has given for a post
def check_what_vote(post_id, user_id):
    try:
        post_data = PostVoteUpdate.objects.filter(post_id=post_id, user=user_id).first()

        if post_data:
            return post_data.voted_as
        else:
            return None
    except Exception as e:
        return None


@login_required
def delete_post(request, **kwargs):
    id = kwargs['pk']
    post_details = UserPostModel.objects.get(id=id)
    file_name = post_details.image_post
    try:
        post_details.delete()
    except Exception as e:
        print (e)

    if file_name:
        if str(os.environ.get("USE_PRODUCTION_SERVICES")) == '1':
            import boto3
            s3_client = boto3.resource('s3',
                             aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                             aws_secret_access_key= os.environ.get('AWS_SECRET_ACCESS_KEY'))
            key = 'static/'+str(file_name)
            my_object = s3_client.Object(os.environ.get('AWS_STORAGE_BUCKET_NAME'), key)
            a = my_object.delete()

        else:
            os.remove(os.path.join(settings.MEDIA_ROOT, str(file_name)))
    return  HttpResponse(f"<div><div>")




def check_and_update_post_votes(post_id, user_id, vote_type):
    post_data = PostVoteUpdate.objects.filter(post_id=post_id, user=user_id).first()
    post_model = UserPostModel.objects.get(id=post_id)
    user_model = User.objects.get(username=user_id)

    if post_data:
        user_has_voted_for = post_data.voted_as
        #removes the post vote if user has already voted for it
        if user_has_voted_for==vote_type:
            post_data.delete()

        return user_has_voted_for

    else:
        PostVoteUpdate.objects.create(post_id=post_model, user=user_model, voted_as=vote_type)
        return "first_upvote"


@login_required
def postupvoteupdate(request, **kwargs):
    id = kwargs['pk']
    post_details = UserPostModel.objects.get(id=id)
    #upvote_current --> has the total upvote count for the post from post_details
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


@login_required
def postdownvoteupdate(request, **kwargs):
    id = kwargs['pk']
    post_details = UserPostModel.objects.get(id=id)
    #downvote_current --> has the total upvote count for the post from post_details
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


@login_required
def homefeedview(request):
    current_user = request.user
    posts = UserPostModel.objects.all()
    # paginator = Paginator(posts, 3)
    final_data = []

    for i in posts:
        data_to_append = i.__dict__
        data_to_append["vote"] = check_what_vote(i.id, request.user)
        data_to_append["user_name"] = i.user_name
        print("----->",dir(UserAccountModel.objects.get(user_name=i.user_name).profile_image))
        try:
            data_to_append["user_image"] = str(UserAccountModel.objects.get(user_name=i.user_name).profile_image)
            print(data_to_append)
        except Exception as e:
            print(e)
        final_data.append(data_to_append)

    # paginator = Paginator(test_data, 3)

    context = {
        'c_user':current_user,
        'data':final_data, 
    }
    return render(request, 'homefeed/home.html', context)


@login_required
def postupload(request):
    if request.method == 'POST':
        user_object = User.objects.get(username=request.user)
        if 'image_upload' in request.FILES:  
            uploaded_file_size = request.FILES['image_upload'].size/ 1024 / 1024
            if uploaded_file_size<3:
                if str(request.FILES['image_upload']).rsplit('.', 1)[-1] in ['jpeg', 'png', 'gif', 'jpg']:
                    post_created = UserPostModel.objects.create(user_name=user_object,
                                        post_text=request.POST['user_post'],
                                        image_post=request.FILES['image_upload'])
            else:
                return redirect(homefeedview)

        else:
            post_text = request.POST['user_post']
            if not set(post_text)=={" "}:
                if len(post_text):
                    post_created = UserPostModel.objects.create(user_name=user_object,
                                                post_text=request.POST['user_post'])
            # do nothing if text is empty while posting(i.e. if witout a upload)
            else:
                pass
        return redirect(homefeedview)


