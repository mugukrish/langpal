from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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


