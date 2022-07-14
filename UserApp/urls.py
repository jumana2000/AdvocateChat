from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('find_lawyer/<str:law>/',views.find_lawyer,name='find_lawyer'),
    path('profile/<int:id>/',views.profile,name='profile'),
    path('book-a-consultation',views.book_consultation,name='book_consultation'),
    path('user_register',views.user_register,name='user_register'),
    path('u_register',views.u_register,name='u_register'),
    path('user_login',views.user_login,name='user_login'),
    path('u_login',views.u_login,name='u_login'),
    path('lawyer_register',views.lawyer_register,name='lawyer_register'),
    path('l_register',views.l_register,name='l_register'),
    path('u_logout',views.u_logout,name='u_logout')
]
