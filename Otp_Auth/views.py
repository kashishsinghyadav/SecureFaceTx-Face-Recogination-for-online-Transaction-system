
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from .models import OTP

def otpauth(request):
    return render(request, 'faceDetection/otp.html')

def send_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = get_random_string(length=6, allowed_chars='1234567890')
        OTP.objects.update_or_create(email=email, defaults={'otp': otp})
        send_mail(
            'OTP Verification',
            f'Your OTP is: {otp}',
            'kashishsinghy@gmail.com',  # replace with your email
            [email],
            fail_silently=False,
        )
        return render(request, 'faceDetection/otp_sent.html', {'email': email})
    return redirect('otpauth')  

def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp_entered = request.POST.get('otp')
        try:
            otp_obj = OTP.objects.get(email=email, otp=otp_entered)
            otp_obj.delete()
            return redirect('otpauth')
        except OTP.DoesNotExist:
            pass
    return render(request, 'faceDetection/verify_otp.html')



# Create your views here.