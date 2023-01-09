from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, auth 
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views import View

from .models import UserAccountModel


#below function checks if username is availabe when enterned in the login form
def check_if_username_availabe(request):
    try:
        username = request.POST.get('username')

        if len(username)<5:
            return HttpResponse('<div class="text-red-500 italic">Username should contain atleast 5 characters!</div>')
        if User.objects.filter(username=username).first():
            return HttpResponse('<div class="text-red-500 italic">Username already taken!</div>')
        else:
            return HttpResponse('<div class="text-green-400 italic">Username available!</div>')
    except Exception as e:
        print(e)
        raise Http404("Page not found")


#below function checks if email is availabe when enterned in the login form
def check_email(request):
    try:
        email = request.POST.get('email')
        if len(email)>3:
            if User.objects.filter(email=email).first():
                return HttpResponse('<div class="text-red-500 italic">email already taken!</div>')
            else:
                return HttpResponse("")
        else:
            return HttpResponse("")
    except Exception as e:
        print(e)
        raise Http404("Page not found")


def logoutview(request):
    logout(request)
    return redirect('account_home_view')



class AccountHomeView(View):
    template = 'account/loginhome.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('homefeed')
        return render(request, self.template)


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
        if request.user.is_authenticated:
            return redirect('login_view')
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
            return redirect('homefeed')
        return render(request, self.template, {'message':'Username or password is not correct'})


class UserUpdate(LoginRequiredMixin, View):
    template = 'account/userupdate.html'
    
    def get(self, request):
        context = {}
        user_details = UserAccountModel.objects.get(user_name=request.user)
        context["userdetails"] = user_details
        return render(request, self.template, context)
    
    def post(self, request):
        context = {}
        user_details = UserAccountModel.objects.get(user_name=request.user)
        user_details.about_me = request.POST['aboutme']

        if 'image_upload' in request.FILES:  
            user_details.profile_image = request.FILES['image_upload']

        if request.POST['country'] is not '0':
            user_details.location = request.POST['country']
        else:
            user_details.location = ''

        user_details.save()
        context["userdetails"] = user_details
        return render(request, self.template, context)



