from django.urls import path

from .views import testhtmx, postupvoteupdate, postdownvoteupdate


urlpatterns = [
    path('dydata/<int:page>', testhtmx, name='testhtmx'),
    path('upvote/<uuid:pk>', postupvoteupdate, name='upvote'),
    path('downvote/<uuid:pk>', postdownvoteupdate, name='downvote'),
]