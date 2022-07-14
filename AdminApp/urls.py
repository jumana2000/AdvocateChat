from django.urls import path
from . import views

urlpatterns = [
    path('adminindex',views.adminindex,name='adminindex'),
    path('addlaw',views.addlaw,name='addlaw'),
    path('law_data',views.law_data,name='law_data'),
    path('lawyer_request',views.lawyer_request,name='lawyer_request'),
    path('approve_lawyer/<int:id>/',views.approve_lawyer,name='approve_lawyer'),
    path('user_request',views.user_request,name='user_request'),
    path('approve_user/<int:id>/',views.approve_user,name='approve_user'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adlogin',views.adlogin,name='adlogin'),
    path('adminlogout',views.adminlogout,name='adminlogout')
]
