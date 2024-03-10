
from django.shortcuts import render,redirect
from Face_Detection.detection import FaceRecognition
from django.contrib import messages
from django.http import HttpResponse
from .models import Creditmodel,Bankmodel
from Face_Detection.models import UserProfile
# Create your views here.
def credit(request,face_id):
    try:

        face_id=int(face_id)
        user_profile = {
                'user': UserProfile.objects.get(face_id=face_id)
            }
    except UserProfile.DoesNotExist:
        raise HttpResponse("UserProfile does not exist")
    return render(request,'faceDetection/transactionpage.html')

def process_payment(request):
    if request.method=='POST':
        charge_type=request.POST.get('chargeType')
        if charge_type=='credit':
            name_on_card = request.POST.get('nameOnCard')
            card_number = request.POST.get('cardNumber')
            expiry_mm = request.POST.get('expiry_mm')
            cvv = request.POST.get('cvv')
            userdata=Creditmodel(name_on_card=name_on_card,card_number=card_number,expiry_mm =expiry_mm ,cvv=cvv)
            userdata.save()
        elif charge_type=='bank':
            account_holder = request.POST.get('accountHolder')
            routing_number = request.POST.get('routing')
            account_type = request.POST.get('accountType')
            userinfo=Bankmodel(account_holder=account_holder,routing_number=routing_number,account_type =account_type)
            userinfo.save()

        return redirect('otpauth')
    
    else:
        return HttpResponse("Method not allowed.", status=405)


        



