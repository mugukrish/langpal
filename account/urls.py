from django.urls import path

from .views import SignupView, LoginLogoutView, AccountHomeView


urlpatterns = [
    path('', AccountHomeView.as_view(), name='account_home_view'),
    path('login/', LoginLogoutView.as_view(), name='login_view'),
    path('signup/', SignupView.as_view(), name='signup_view'),
    path('logout/', LoginLogoutView.as_view(), name='logout_view'),
]