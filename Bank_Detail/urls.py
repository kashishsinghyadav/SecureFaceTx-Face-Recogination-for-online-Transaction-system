from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('credit/<int:face_id>/',credit,name='credit'),
    path('process_payment/',process_payment,name='process_payment')
]
