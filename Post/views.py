from email.headerregistry import Group
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from Login.views import user_login
from .models import Post
from .forms import PostForm, UpdateForm


def home(request):
    show_rec = Post.objects.all()
    return render(request, "Blog_Home.html", {'show_rec':show_rec})

def userdashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        group =  user.groups.all()
        return render(request, "UserDashboard.html",{'posts':posts,'full_name':full_name,'groups':group,})
    else:
        return HttpResponseRedirect('/login/')

def blogview(request,pk): #For viewing each post by using primary key
    if request.user.is_authenticated:    
        rec = Post.objects.get(pk=pk)
        return render(request, 'Each_blog.html', {'rec':rec})
    else:
        return HttpResponseRedirect('/login/')
def add_posts(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid:
                form.save()
                return HttpResponseRedirect('/userdashboard/')
        else:
            form = PostForm()
        return render(request,'add_posts.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def update_rec(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            rec = Post.objects.get(pk=id)
            form = UpdateForm(request.POST, instance=rec)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/userdashboard/')
        else:
            rec = Post.objects.get(pk=id)
            form = UpdateForm(instance=rec)
        return render(request, 'update.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

def delete_rec(request, id):
    if request.user.is_authenticated:
        dele = Post.objects.get(id=id)
        dele.delete()
        return HttpResponseRedirect('/userdashboard/')
    else:
        return HttpResponseRedirect('/login/')

def About_us(request):
    return render(request,'About_us.html')
