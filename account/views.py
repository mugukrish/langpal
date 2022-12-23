from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.contrib.auth import logout
from django.views import View
from django.http import HttpResponse

from .models import UserAccountModel
from homefeed import views


def check_username(request):
    username = request.POST.get('username')

    if len(username)<5:
        return HttpResponse('<div class="text-red-500 italic">Username should contain atleast 5 characters!</div>')
    if User.objects.filter(username=username).first():
        return HttpResponse('<div class="text-red-500 italic">Username already taken!</div>')
    else:
        return HttpResponse('<div class="text-green-400 italic">Username available!</div>')


def check_email(request):
    email = request.POST.get('email')
    if len(email)>3:
        if User.objects.filter(email=email).first():
            return HttpResponse('<div class="text-red-500 italic">email already taken!</div>')
        else:
            return HttpResponse("")
    else:
        return HttpResponse("")



class AccountHomeView(View):
    template = 'account/loginhome.html'

    def get(self, request):
        context = {}
        print('came here')
        return render(request, self.template, context)


class SignupView(View):
    template = 'account/signup.html'
    
    def post(self, request):
        context = {}
        username = request.POST['username']
        email = request.POST['email'].lower()
        dob = request.POST['dob']
        password = request.POST['password1']
        password_2 = request.POST['password2']

        #validation
        if User.objects.filter(username=username).first():
            context['username_exist'] = "User name already exists"
        elif len(username)<5:
            context['username_length'] = 'User name length should be greater than 4'

        if User.objects.filter(email=email).first():
            context['email_exists'] = 'Emial already exists'

        if password == password_2:
            if len(password)<8:
                context['password_lenght'] = 'Password shoudl contain more than 7 characters'
        else:
            context['password_match'] = 'Password does not match'
        
        
        if len(context)>0:
            return render(request, self.template, context = {'object':context})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            user_model = User.objects.get(username=username)
            profile = UserAccountModel.objects.create(user_name=user_model,email=user_model.email ,id_user=user_model.id, dob=dob)
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
        return render(request, self.template, {'message':'Username or password is not correct'})


def logoutview(request):
    logout(request)
    return redirect('account_home_view')

