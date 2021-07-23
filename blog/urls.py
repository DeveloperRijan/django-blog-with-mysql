from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login_writer, name="login"),
    path('logout/', views.logout_writer, name="logout"),
]
