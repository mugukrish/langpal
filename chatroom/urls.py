from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.allroomlist, name='all_rooms'),
    path('<slug:slug>/', views.joinroom, name='join_room')
]
