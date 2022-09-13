from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
 
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('register/',views.registerpage,name='register'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.loginpage,name='logout'),
]
