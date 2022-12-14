from django.shortcuts import render
from .models import ChatRoomsList
# Create your views here.


def allroomlist(request):
    context = {}
    roomslist = ChatRoomsList.objects.all()
    context['objects'] = roomslist
    return render(request, 'chatroom/alltherooms.html', context)


def joinroom(request, slug):
    context = {}
    room = ChatRoomsList.objects.get(slug=slug)
    context['room'] = room
    return render(request, 'chatroom/joinroom.html', context)