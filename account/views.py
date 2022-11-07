from django.shortcuts import render
from django.contrib.auth.models import User, auth 

from .models import UserAccountModel

# Create your views here.

def loginhomeview(request):
    context = {}
    return render(request, 'account/loginhome.html', context)

def signupview(request):
    context = {}
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        email = data['email']
        dob = data['dob']
        password = data['password1']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        user_model = User.objects.get(username=username)
        profile = UserAccountModel.objects.create(user_name=user_model, id_user=user_model.id, dob=dob)
        profile.save()
    return render(request, 'account/signup.html', context)

def loginview(request):
    context = {}
    return render(request, 'account/login.html', context)
