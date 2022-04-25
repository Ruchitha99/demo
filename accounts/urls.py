from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as a_views

urlpatterns = [
path('login/', views.login, name='login'),
path('logout/',views.logout,name='logout'),
path('signin/', views.signin, name='signin'),
path('signout/',views.signout,name='signout'),
]

