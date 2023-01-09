from django.urls import path, include

from .views import return_meaning_from_dictionaryapi

urlpatterns = [
    path('', return_meaning_from_dictionaryapi, name='wordapp_home'),
]
