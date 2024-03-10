from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name = "home"),
    path('register/',register,name = 'register'),
    path('login/',login,name = 'login'),
    path('greeting/<face_id>/',Greeting,name='greeting'),
    path('profile/<int:face_id>/', profile_view, name='profile'),
]
