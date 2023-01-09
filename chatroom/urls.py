from django.urls import path, include

from .views import allroomlist, joinroom, create_room

urlpatterns = [
    path('', allroomlist, name='all_rooms'),
    path('createroom/', create_room, name='create_room'),
    path('<slug:slug>/', joinroom, name='join_room')
]
