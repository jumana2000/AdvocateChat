from django.urls import path
from . import views

urlpatterns = [
    path('adminindex',views.adminindex,name='adminindex'),
    path('',views.adminlogin,name='adminlogin'),
    path('adlogin',views.adlogin,name='adlogin'),
    path('adminlogout',views.adminlogout,name='adminlogout')
]
