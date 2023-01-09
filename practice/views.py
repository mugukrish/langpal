from django.shortcuts import render, redirect
from wordbox.models import MeaningSentences
from random import choice
from django.contrib.auth.decorators import login_required


@login_required
def practice_home(request):
    if request.method == 'POST':
        return redirect(create_new_room)
    return render(request, 'practice/rooms.html')

@login_required
def create_new_room(request):
    context = {
        "roomname": 'test'
    }
    return render(request, 'practice/createroom.html', context)

@login_required
def learn_by_reading(request):
    #randomly select an scentence from MeaningSentences DB and pass to textarea in frontend
    data = MeaningSentences.objects.values_list('id', flat=True)
    random_id = choice(data)
    random_obj = MeaningSentences.objects.get(id=random_id).sentence
    context = {"sentence":random_obj}

    return render(request, 'practice/learnbyreading.html', context)