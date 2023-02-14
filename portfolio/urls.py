from django.urls import path

from .views import portfolio_home_view

urlpatterns = [
    path('', portfolio_home_view, name='portfolio_home'),
]