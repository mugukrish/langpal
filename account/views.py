from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.contrib.auth import logout
from django.views import View

from .models import UserAccountModel
from homefeed import views
# Create your views here.


class AccountHomeView(View):
    template = 'account/loginhome.html'

    def get(self, request):
        context = {}
        print('came here')
        return render(request, self.template, context)


class SignupView(View):
    template = 'account/signup.html'
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        dob = request.POST['dob']
        password = request.POST['password1']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        user_model = User.objects.get(username=username)
        profile = UserAccountModel.objects.create(user_name=user_model, id_user=user_model.id, dob=dob)
        profile.save()
        return render(request, self.template)
    
    def get(self, request):
        return render(request, self.template)


class LoginView(View):
    template = 'account/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('homefeed')
        return render(request, self.template)

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user:
            auth.login(request, user)
            return redirect(views.homefeedview)
        context = {}
        return redirect(request, 'account/login.html', context)


def logoutview(request):
    logout(request)
    return redirect('account_home_view')

