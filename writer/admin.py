from django.contrib import admin

from .models import *

#admin ui modification
class PostUI(admin.ModelAdmin):
    list_display = ('writer', 'category', 'title',)


# Register your models here.
admin.site.register(Post, PostUI)