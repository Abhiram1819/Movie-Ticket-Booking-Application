from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        user_name = request.POST['Username']
        email = request.POST['Email']
        password = request.POST['Password']
        ConfirmPassword = request.POST['Password1']

        if password == ConfirmPassword:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        user_name = request.POST['Username']
        password = request.POST['Password']

        user = auth.authenticate(username=user_name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def admin_login(request):
    if request.method == 'POST':
        user_name = request.POST['Username']
        password = request.POST['Password']

        user = auth.authenticate(username=user_name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('admin_page')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('admin_login')
    else:
        return render(request,'admin_login.html')
    return render(request,'admin_login.html')

def admin_page(request):
    return render(request,'admin_page.html')

def admin_logout(request):
    auth.logout(request)
    return redirect('admin_login')
