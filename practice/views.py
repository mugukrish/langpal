from django.shortcuts import render, redirect

# Create your views here.

def practice_home(request):
    if request.method == 'POST':
        return redirect(create_new_room)
    return render(request, 'practice/rooms.html')

def create_new_room(request):
    context = {
        "roomname": 'test'
    }
    return render(request, 'practice/createroom.html', context)

def learn_by_reading(request):
    context = {}
    return render(request, 'practice/learnbyreading.html', context)