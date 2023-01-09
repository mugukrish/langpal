from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import AboutIdeaPostModel

#Store the idea submitted in DB
@login_required()
def post_idea_from_about(request):
    if request.method == 'POST':
        user_model = User.objects.get(username=request.user)
        AboutIdeaPostModel.objects.create(user_name=user_model,
                                        idea_title = request.POST['ideatitle'],
                                        idea_text=request.POST['ideadescription']
                                        )
        return redirect('about_home')
    return redirect('about_home')

@login_required()
def about_page(request):    
    ideas_data = AboutIdeaPostModel.objects.all()
    context = {"ideas":ideas_data}
    return render(request, 'about/about_no.html', context)


def update_idea_vote_count(request, **kwargs):
    current_idea = AboutIdeaPostModel.objects.get(id=kwargs['pk'])
    current_votes_for_idea = current_idea.idea_votes
    current_votes_for_idea+=1
    current_idea.idea_votes = current_votes_for_idea
    
    current_idea.save()
    return HttpResponse(f'({current_votes_for_idea})')
    


