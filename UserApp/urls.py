from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('user_register',views.user_register,name='user_register'),
    path('u_login',views.u_login,name='u_login')
]
