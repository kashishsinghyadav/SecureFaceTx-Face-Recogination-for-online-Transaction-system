
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

def otpauth(request):
    return render(request,'faceDetection/otp.html')





# Create your views here.