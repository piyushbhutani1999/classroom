
from django.urls import path
from django.contrib.auth import authenticate, login,logout
from . import views
from django.conf.urls import url


app_name="customuser"

urlpatterns = [
    path('', views.homepageview, name= 'homepage'),
    path('contact/', views.contactus, name = 'contact'),
    path('login/', views.login_view, name = 'login'),
    path('signup/', views.signup_view, name = 'signup'),
  
]