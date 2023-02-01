from django.forms import PasswordInput
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrtionForm, LoginForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import Group

def register(request):
    if request.method == 'POST':
        fm = RegistrtionForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Registration Successfull')
            user = fm.save()
            group = Group.objects.get(name='User Group')
            user.groups.add(group)
            return HttpResponseRedirect('/')
    else:
        fm = RegistrtionForm()
    return render(request,'enroll/Register.html',{'form':fm})

def user_login(request):
    if not request.user.is_authenticated: #if the user is already logged in then does'nt allow the user to login again unless user logout and login again
        if request.method == 'POST':
            fm = LoginForm(request=request, data=request.POST) 
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                pwd = fm.cleaned_data['password']
                user = authenticate(username=uname, password=pwd)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/userdashboard/')
        else:
            fm = LoginForm()
        return render(request, 'enroll/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')