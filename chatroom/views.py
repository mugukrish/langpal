from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatRoomsList, UserMessage


@login_required
def create_room(request):
    context = {}
    if request.method == 'POST':
        room_name = name=request.POST['roomname'].strip()
        if not ChatRoomsList.objects.filter(name=room_name).first():
            ChatRoomsList.objects.create(name=room_name,
                                        slug=room_name,
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
    context['current_user_from_view'] = str(request.user)
    context['room'] = room
    context['old_messages'] = messages_history


    return render(request, 'chatroom/joinroom.html', context)