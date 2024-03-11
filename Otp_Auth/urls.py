from django.contrib import admin
from django.urls import path
from Otp_Auth.views import otpauth,send_otp,verify_otp
urlpatterns = [
    path('otpauth/',otpauth,name='otpauth'),
    path('send_otp/', send_otp, name='send_otp'),  # URL for sending OTP (initial page)
    path('verify_otp/', verify_otp, name='verify_otp'),  # URL for verifying OTP

    
]
