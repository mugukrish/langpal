from django.shortcuts import render
from .models import ChatRoomsList, UserMessage
# Create your views here.


def allroomlist(request):
    context = {}
    roomslist = ChatRoomsList.objects.all()
    context['objects'] = roomslist
    return render(request, 'chatroom/alltherooms.html', context)


def joinroom(request, slug):
    context = {}
    room = ChatRoomsList.objects.get(slug=slug)
    context['user'] = str(request.user)
    context['room'] = room
    context['old_messages'] = UserMessage.objects.filter(room=room)[:25]

    return render(request, 'chatroom/joinroom.html', context)