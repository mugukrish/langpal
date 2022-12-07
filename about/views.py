from django.shortcuts import render, redirect
from .models import AboutIdeaPostModel

# Create your views here.

def about_page(request):

    if request.method == 'POST':
        post_created = AboutIdeaPostModel(user_name=request.user,
                                    post_text=request.POST['user_idea_post'])
        post_created.save()
    

    return render(request, 'about/about_no.html')


