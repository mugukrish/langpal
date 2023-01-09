from django.urls import path
from .views import about_page, post_idea_from_about

urlpatterns = [
    path('', about_page, name='about_home'),
    path('idea/', post_idea_from_about, name='about_idea'),
]

