from django.urls import path

from .views import SignupView, LoginView, AccountHomeView,logoutview, check_username, check_email


urlpatterns = [
    path('', AccountHomeView.as_view(), name='account_home_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('signup/', SignupView.as_view(), name='signup_view'),
    path('logout/', logoutview, name='logout_view'),
    path('check_username/', check_username, name='check_username'),
    path('check_email/', check_email, name='check_email'),

]