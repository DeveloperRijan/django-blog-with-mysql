from django.urls import path

from . import views

urlpatterns = [
    path("writer/dashboard/", views.dashboard, name='writer.dashboard'),
    path("writer/new-post/", views.post_new, name='writer.post.new'),
    path("writer/posts/", views.posts, name='writer.posts'),
    path("writer/post/edit/<int:post_id>", views.post_edit, name='writer.post.edit'),
]
