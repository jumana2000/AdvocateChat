from django.http import HttpResponse
from . models import *
from django.shortcuts import render,redirect
from AdminApp.models import *
# Create your views here.

def index(request):
    data = Law.objects.all()
    return render(request,'index.html',{'data':data})

def find_lawyer(request,law):
    data1 = LRegister.objects.filter(law=law,status=1)
    data = Law.objects.all()
    return render(request,'lawyer_list.html',{'data1':data1,'data':data})

def profile(request,id):
    profile_data = LRegister.objects.filter(id=id)
    data = Law.objects.all()
    return render(request,'profile.html',{'profile_data':profile_data,'data':data})

def book_consultation(request):
    data = Law.objects.all()
    return render(request,'book_consultation.html',{'data':data})

def user_register(request):
    return render(request,'user_register.html')

def u_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password= request.POST.get('password')
        data = Register(name=name,email=email,phone=phone,password=password)
        data.save()
    return redirect('user_login')

def user_login(request):
    return render(request,'user_login.html')

def u_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if Register.objects.filter(email=email,password=password,status=1).exists():
        return redirect('index')

    elif LRegister.objects.filter(email=email,password=password,status=1).exists():
        return redirect('index')
    
    else:
        return redirect('user_login')

def u_logout(request):
    return redirect('index')

def lawyer_register(request):
    return render(request,'lawyer_register.html')

def l_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        enrollment_no = request.POST.get('enrollment_no')
        password= request.POST.get('password')
        data = LRegister(name=name,email=email,phone=phone,password=password,enrollment_no=enrollment_no)
        data.save()
    return redirect('user_login')