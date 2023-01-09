from django.urls import path

from .views import SignupView, LoginView, AccountHomeView,UserUpdate
from .views import logoutview, check_if_username_availabe, check_email


urlpatterns = [
    path('', AccountHomeView.as_view(), name='account_home_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('signup/', SignupView.as_view(), name='signup_view'),
    path('userupdate/', UserUpdate.as_view(), name='userupdate_view'),
    path('logout/', logoutview, name='logout_view'),
    path('check_username/', check_if_username_availabe, name='check_username'),
    path('check_email/', check_email, name='check_email'),

]