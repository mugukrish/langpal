from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatRoomsList, UserMessage


@login_required
def create_room(request):
    if request.method == 'POST':
        ChatRoomsList.objects.create(name=request.POST['roomname'],
                                    slug=request.POST['roomname'],
                                    description=request.POST['roomdescription'])
    return redirect('all_rooms')

@login_required
def allroomlist(request):
    context = {}
    roomslist = ChatRoomsList.objects.all()
    context['objects'] = roomslist
    return render(request, 'chatroom/alltherooms.html', context)

@login_required
def joinroom(request, slug):
    context = {}
    room = ChatRoomsList.objects.get(slug=slug)
    messages_history = UserMessage.objects.filter(room=room).order_by('-date_added')
    context['user'] = str(request.user)
    context['room'] = room
    context['old_messages'] = messages_history


    return render(request, 'chatroom/joinroom.html', context)