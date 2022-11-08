from django.urls import path

from . import views


urlpatterns = [
    path('', views.loginhomeview),
    path('login/', views.loginview, name='login_view'),
    path('signup/', views.signupview, name='signup_view'),
    path('logout/', views.logoutview, name='logout_view'),
]