from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    return render(request, "writer/dashboard.html")


# add new post
def post_new(request):
    return render(request, "writer/pages/posts/new.html")


#get list of post
def posts(request):
    pass