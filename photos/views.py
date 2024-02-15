from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from .models import Photos


def RedirectToPhotowall(request):
    return redirect(reverse('photos:photos'))


@login_required
def UploadPhoto(request):
    try:
        if request.method == 'POST':
            pictures = request.FILES.get('upload_photo')
            Photos.objects.create(filepath=pictures,
                                    uploaded_by=request.user.username)
            
            print(f"User {request.user.username} has uploaded a photo!")
            return redirect(reverse('photos:photos'))
            
        elif request.method == 'GET':
            return render(request, 'uploadform.html')
        
    except Exception as err:
        print(f"Error while uploading a photo: {err}")
   

   
@login_required
def ViewPhotos(request):
    try:
        username = request.user.username
        photos = Photos.objects.filter(uploaded_by=username)
        return render(request, 'photos.html', {"photos": photos,
                                               "username": username})
    except Exception as err:
        print(f"Error in photowall: {err}")     
    


def SignUpUser(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            if User.objects.filter(username=username).exists():
                return render(request, 'signup.html', {"already_exists": True})
            
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            
            user.save()
            
            print(f'User {username} is successfully created')
            return redirect(reverse('photos:login'))
        elif request.method == 'GET':
            return render(request, 'signup.html')
    except Exception as err:
        print(f'Error while signing up the user: {err}')   
        
def LogInUser(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username,
                                     password=password)
            if user:
                auth.login(request, user)
                
                print(f"User {username} is logged in!")
                return redirect(reverse('photos:photos'))
            
            print(f"User entered invalid credentials")
            return render(request, 'login.html', {'invalid_user': True})
        elif request.method == 'GET':
            return render(request, 'login.html')
    except Exception as err:
        print(f"Error while logging in: {err}")
        
def LogOutUser(request):
    try:
        print(f"User {request.user.username} is logging out")
        auth.logout(request)
        return redirect(reverse('photos:login'))
    except Exception as err:
        print(f"Error while logging out: {err}")

