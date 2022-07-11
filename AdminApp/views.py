from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.

def adminindex(request):
    return render(request,'adminindex.html')

def adminlogin(request):
    return render(request,'adminlogin.html')

def adlogin(request):
    username_a = request.POST.get('username')
    password_a = request.POST.get('password')
    if User.objects.filter(username__contains=username_a).exists():
        user = authenticate(username=username_a,password=password_a)
        if user is not None:
            login(request,user)
            request.session['username_a'] = username_a
            request.session['password_a'] = password_a
            print(user)
            return redirect('adminindex')
        else:
            return render(request,'adminlogin.html',{'msg':"Sorry... Invalid username or password"})
    else:
        return render(request,'adminlogin.html',{'msg':"Sorry... Invalid username or password"})

def adminlogout(request):
    del request.session['username_a']
    del request.session['password_a']
    return redirect('adminlogin')