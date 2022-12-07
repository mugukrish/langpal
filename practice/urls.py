from django.urls import path
from . import views

urlpatterns = [
    path('', views.practice_home, name='practicehome'),
    path('room/', views.create_new_room, name='newroom'),
]

