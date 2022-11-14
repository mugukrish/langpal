from django.urls import path

from .views import SignupView, LoginView, AccountHomeView, logoutview


urlpatterns = [
    path('', AccountHomeView.as_view(), name='account_home_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('signup/', SignupView.as_view(), name='signup_view'),
    path('logout/', logoutview, name='logout_view'),
]