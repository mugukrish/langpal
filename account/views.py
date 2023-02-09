from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, auth 
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views import View

import os

from .models import UserAccountModel


#below function checks if username is availabe when enterned in the login form
def check_if_username_availabe(request):
    username = request.POST.get('username')
    try:
        if len(username)==0:
            return HttpResponse('<div></div>')
        if " " in username:
            return HttpResponse('<div class="text-red-500 italic">Username should not contain blankspaces</div>')
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
        age = request.POST['age']
        password = request.POST['password1']
        password_2 = request.POST['password2']

        #validation
        if " " in username:
            return render(request, self.template, {'message':'Username should not contain any spaces'})
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
        
        if not 3<=int(age)<=120:
            context['age_match'] = 'Enter a valid age (greater than or equal to 3)'

        if len(context)>0:
            return render(request, self.template, context = {'object':context})
        else:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user_model = User.objects.get(username=username)
                profile = UserAccountModel.objects.create(user_name=user_model,email=user_model.email ,id_user=user_model.id, age=age)
            except Exception as e:
                try:
                    user.delete()
                except Exception as euser:
                    print(euser)
                try:
                    profile.delete()
                except Exception as eprofile:
                    print(eprofile)
                print(e)
                message = "There was an error while creating the user, kindly try after sometime."
                return render(request, self.template, context = {'fatal_error':message})

            return redirect('login_view')
    
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
            if str(request.FILES['image_upload']).rsplit('.', 1)[-1] in ['jpeg', 'png', 'gif', 'jpg']:
                current_profile_image = user_details.profile_image
                user_details.profile_image = request.FILES['image_upload']
                

                

        if request.POST['country'] is not '0':
            user_details.location = request.POST['country']
        else:
            user_details.location = ''

        user_details.save()

        # photo is being currently used, should work on the below delete
        # if 'blank-profile-picture.png' not in current_profile_image:
        #             os.remove(os.path.join(settings.MEDIA_ROOT, str(current_profile_image)))
        context["userdetails"] = user_details
        return render(request, self.template, context)


