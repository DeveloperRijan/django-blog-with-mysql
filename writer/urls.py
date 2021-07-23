from django.urls import path

from . import views

urlpatterns = [
    path("writer/dashboard/", views.dashboard, name='writer.dashboard')
]
