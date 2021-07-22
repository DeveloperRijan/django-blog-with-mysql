from django import http
from django.conf.urls import url
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import RequestContext


# Create your views here.

#Home Page
def home(request):
    return render(request, "frontend/index.html")



#Register of writers
def register(request):
    if(request.method != 'POST'):
        return render(request, "frontend/register.html")
    
    #if post then validate data
    error = False
    error_msg = []

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    if(first_name == ''):
        error = True
        error_msg.append("The first name field is required")
    
    if(last_name == ''):
        error = True
        error_msg.append("The last name field is required")
    
    if(username == ''):
        error = True
        error_msg.append("The username field is required")
    
    if(email == ''):
        error = True
        error_msg.append("The email field is required")
    
    if(password == ''):
        error = True
        error_msg.append("The password field is required")

    #validate username is already exists or not
    if(User.objects.filter(username=username).first() != None):
        error = True
        error_msg.append("The username is already taken")
    
    if(User.objects.filter(email=email).first() != None):
        error = True
        error_msg.append("The email is already taken")
    
    if(error == True):
        messages.info(request, error_msg[0])
        return redirect('/register')

    #if validation pass then save data
    User.objects.create(
        password=password,
        is_superuser=0, 
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        is_staff=0,
        is_active=1
    )
    messages.success(request, 'Registration Completed')
    return redirect('/register')



#login
def login(request):
    return render(request, "frontend/login.html")