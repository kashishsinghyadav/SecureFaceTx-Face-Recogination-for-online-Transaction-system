from django.shortcuts import render,redirect
from Face_Detection.detection import FaceRecognition
from .forms import *
from django.contrib import messages
from .models import UserProfile
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required  


faceRecognition = FaceRecognition()

def profile_view(request, face_id):
    try:
        face_id = int(face_id)
        user_profile = {
            'user': UserProfile.objects.get(face_id=face_id)
        }
    except UserProfile.DoesNotExist:
        raise HttpResponse("UserProfile does not exist")
    
    return render(request, 'faceDetection/userpro.html', {'user_profile': user_profile})



def home(request):
    return render(request,'faceDetection/home.html')


def register(request):
    try:

        if request.method == "POST":
            face_id = request.POST.get('face_id')
            name = request.POST.get('name')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            image = request.FILES.get('image')
            user_profile = UserProfile(
                face_id=face_id,
                name=name,
                address=address,
                phone=phone,
                email=email,
                image=image
            )
            user_profile.save()
            addFace(request.POST['face_id'])

            return redirect('login')


    

        return render(request, 'faceDetection/register.html')
    except:
        return render(request, 'faceDetection/register.html')

def addFace(face_id):
    face_id = face_id
    faceRecognition.faceDetect(face_id)
    faceRecognition.trainFace()
    return redirect('/')
def login(request):
    face_id = faceRecognition.recognizeFace()
    print(face_id)
    return redirect('greeting' ,str(face_id))
    
    
    
   
def Greeting(request,face_id):
    face_id = int(face_id)
    context ={
        'user' : UserProfile.objects.get(face_id = face_id)
    }
    return render(request,'faceDetection/greeting.html',context=context)

