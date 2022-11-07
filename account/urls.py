from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.loginview),
    path('signup/', views.signupview),

]

