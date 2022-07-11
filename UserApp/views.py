from ast import Pass
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def user_register(request):
    return render(request,'user_register.html')

def u_login(request):
    pass