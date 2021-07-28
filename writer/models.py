from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL

from blog.models import Category

# Create your models here.
class Post(models.Model):
    writer = models.ForeignKey(User, on_delete=CASCADE)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)
    title = models.CharField(max_length=80)
    body = models.TextField(max_length=20000)
    featured_image = models.ImageField(upload_to='featured_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=1) #active or inactive actions by writer or superadmin
    is_approved = models.BooleanField(default=0) #approved or unapproved actions by superuser/admin only
    is_deleted = models.BooleanField(default=0) #soft delete by writer, but permanent delete will be done by admin

