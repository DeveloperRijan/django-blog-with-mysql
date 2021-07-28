import django
from django.contrib.messages.api import warning
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from PIL import Image
from django.contrib import messages


from blog.models import Category
from .models import Post


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
        return render(request, "writer/pages/posts/add.html", {'categories':categories})
    
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
    
    # if validation pass then
    authUser = request.user
    Post.objects.create(
        title = request.POST['title'],
        body = request.POST['body'],
        featured_image = request.FILES["featured_image"],
        category_id = request.POST["category"],
        writer_id = authUser.id,
    )

    messages.success(request, "Post Created")
    return redirect("/writer/posts")

#get list of post
def posts(request):
    authUser = request.user # current authenticated writer

    posts = Post.objects.filter(writer_id=authUser.id, is_deleted=0).order_by("-created_at").select_related('category').all()   
    return render(request, "writer/pages/posts/index.html", {'posts':posts})



#post edit
def post_edit(request, post_id):
    authUser = request.user # current authenticated writer

    post = Post.objects.filter(id=post_id, writer_id=authUser.id, is_deleted=0).select_related('category').first()
    if(post is None):
        messages.warning(request, "The post not found")
        return redirect("/writer/posts/")
    
    #get categories
    categories = Category.objects.order_by('title').all()
    return render(request, "writer/pages/posts/edit.html", {
        'categories':categories,
        'post':post
    })