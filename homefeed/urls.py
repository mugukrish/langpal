from django.urls import path

from .views import  postupvoteupdate, postdownvoteupdate, delete_post, homefeedview, postupload


urlpatterns = [
    path('', homefeedview, name='homefeed'),
    path('upload/', postupload, name='postupload'),
    path('upvote/<uuid:pk>', postupvoteupdate, name='upvote'),
    path('downvote/<uuid:pk>', postdownvoteupdate, name='downvote'),
    path('deletepost/<uuid:pk>', delete_post, name='delete_post'),
]