from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Home Page
def home(request):
    return render(request, "frontend/index.html")



#Register of writers
def register(request):
    return render(request, "frontend/register.html")



#login
def login(request):
    return render(request, "frontend/login.html")