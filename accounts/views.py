from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def login(request):
    return render(request, 'login.html')
def logout(request):
    return render(request, 'logout.html')
def signin(request):
    return render(request, 'signin.html')
def signout(request):
    return render(request, 'signout.html')