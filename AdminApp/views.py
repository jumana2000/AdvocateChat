from django.shortcuts import render,redirect
from UserApp.models import LRegister,Register
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.

def adminindex(request):
    return render(request,'adminindex.html')

def addlaw(request):
    return render(request,'addlaw.html')

def lawyer_request(request):
    data = LRegister.objects.filter(status=0)
    data1 = LRegister.objects.filter(status=1)
    law = Law.objects.all()
    return render(request,'lawyer_request.html',{'data':data,'data1':data1,'law':law}) 

def approve_lawyer(request,id):
    if request.method == "POST":
        law = request.POST.get('law')
        LRegister.objects.filter(id=id).update(status=1,law=law)
    return redirect('lawyer_request')

def user_request(request):
    data = Register.objects.filter(status=0)
    data1 = Register.objects.filter(status=1)
    return render(request,'user_request.html',{'data':data,'data1':data1})

def approve_user(request,id):
    Register.objects.filter(id=id).update(status=1)
    return redirect('user_request')

def law_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        law_image = request.FILES['law_image']
        data = Law(name=name,law_image=law_image)
        data.save()
    return redirect('addlaw')

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