import django
from django.contrib.messages.api import warning
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from PIL import Image
from django.contrib import messages


from blog.models import Category


# Create your views here.
def dashboard(request):
    if(request.user.is_anonymous):
        return redirect('/login')

    return render(request, "writer/dashboard.html")


# add new post
def post_new(request):
    if(request.user.is_anonymous):
        return redirect('/login')
    
    #get categories
    categories = Category.objects.order_by('title').all()

    #if not post then
    if(request.method != 'POST'):
        return render(request, "writer/pages/posts/new.html", {'categories':categories})
    
    #if method post then validate
    error = False
    error_msg = []

    if(request.POST['category'] != ''):
        #check category is valid
        if(Category.objects.get(id=request.POST['category']) is None):
           error = True 
           error_msg.append("The selected category is invalid")
    
    if(request.POST['title'] == ''):
        error = True 
        error_msg.append("The title field is required")
    elif(len(request.POST['title']) > 80):
        error = True 
        error_msg.append("The title field can't be greater than 80 characters")
    
    if(request.POST['body'] == ''):
        error = True 
        error_msg.append("The body field is required")
    elif (len(request.POST['body']) > 20000):
        error = True 
        error_msg.append("The body field can't be greater than 20000 characters")
    
    if(len(request.FILES) > 0):
        if(request.FILES["featured_image"] is None):
            error = True 
            error_msg.append("Please upload a feature image")
    else:
        error = True 
        error_msg.append("The featured image field is required")

    if(error == True):
        messages.warning(request, error_msg[0])
        return render(request, "writer/pages/posts/new.html", {
            'categories':categories, 
            'old_form_data':request.POST
        })


#get list of post
def posts(request):
    pass