from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from app1.models import *
from django.urls import reverse
import random


# Create your views here.
# from app1.forms import * 

# def User_Auth(request):
#     UFO=UserForm()
#     PFO=ProfileForm()
    

#     d={'UFO':UFO,'PFO':PFO}


#     return render(request,'User_Auth.html',d)
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from app1.forms import * 
from django.core.mail import send_mail
def Auther_View(request):
    UFO=UserForm()
    PFO=ProfileForm()
    d={'UFO':UFO,'PFO':PFO}
    if(request.method=='POST' and request.FILES): 
        UFDO=UserForm(request.POST)
        PFDO=ProfileForm(request.POST,request.FILES)
        if(UFDO.is_valid() and PFDO.is_valid()):
            # User Modification permission
            user_form = UFDO.save(commit=False)
            user_form.set_password(user_form.password)  # Password handling is done automatically by save()
            user_form.save()

             #profile Modification permission
            profile_form = PFDO.save(commit=False)
            profile_form.UserName = user_form  # Link profile to the user
            profile_form.save()
            send_mail('Registration',
            'Thanku For Registration',
            'venkateswarlureddy647@gmail.com',
            [user_form.email],
            fail_silently=False,
             )
            return HttpResponse('registered Succesfully')
        
        else:
            print('UserForm errors:', UFDO.errors)
            print('ProfileForm errors:', PFDO.errors)
            return HttpResponse('Data Invalid')



    return render(request,'User_Auth_Page.html',d)

def HomePage(request):
    if(request.session.get('username')):
        un=request.session.get('username')
        d={'un':un}
        return render(request,'HomePage.html',d)
    return render(request,'HomePage.html')


def LoginPage(request):
    if(request.method=='POST'):
        un=request.POST['un']
        pw=request.POST['pw']
        AUO=authenticate(username=un,password=pw)
        if(AUO):
            login(request,AUO)
            request.session['username']=un
            return HttpResponseRedirect(reverse('HomePage'))
        else:
            return HttpResponse('Invalid Data')
    return render(request,'LoginPage.html')

@login_required
def ProfilePage(request):
    un=request.session.get('username')
    UO=User.objects.get(username=un)
    PO=Profile.objects.get(UserName=UO)
    d={'UO':UO,'PO':PO}
    return render(request,'ProfilePage.html',d)

@login_required
def LogoutPage(request):
    logout(request)
    return HttpResponseRedirect(reverse('HomePage'))
@login_required
def ChangePassword(request):
    if(request.method=='POST'):
        un=request.session['username']
        npw=request.POST['npw']
        rpw=request.POST['rpw']
        if(npw==rpw):
            UO=User.objects.get(username=un)
            UO.set_password(npw)
            UO.save()
            return HttpResponseRedirect(reverse('HomePage'))
        else:
            return HttpResponse('Password Misss Matched')
    return render(request,'ChangePassword.html')


def ResetPasswordPage(request):

    if(request.method=='POST'):
        un=request.POST['un']
        npw=request.POST['npw']
        rpw=request.POST['rpw']
        #fwtching username from model
        try:
            UO=User.objects.get(username=un)
        except User.DoesNotExist:
            print("User not found:", un)
            return HttpResponse('User not found. Please check your username.')
        if(npw==rpw):
            s={1,2,3,4,5,6,7,8,9,0}
            otp=random.randint(1000,9999)
            print(otp)
            UO=User.objects.get(username=un)
            print(UO.username)
            print(';control Here')
            send_mail('Forget Password OTP',
            f"Your Forget Password  Otp is${otp}",
            'venkateswarlureddy647@gmail.com',
            [UO.email],
            fail_silently=False,
            )   
            print('control2')
            request.session['Otp']=otp
            request.session['Password']=rpw
            request.session['Username']=UO.username
            
            return HttpResponseRedirect(reverse('OtpPage'))

        else:
            return HttpResponse('Enter and Agian Password Not Matched\n Try Agian Once')
    
    return render(request,'ResetPasswordPage.html')
                



    return render(request,'ResetPasswordPage.html')
def OtpPage(request):
    if(request.method=='POST'):
        print('otp1')
        Otp=request.session.get('Otp')
        print(Otp,type(Otp))
        otp=int(request.POST['Otp'])
        
        print('otp2')
        print(otp,type(otp))
        username=request.session.get('Username')
        if(Otp==otp):
            pw=request.session.get('Password')
            un=request.session.get('Username')
            UO=User.objects.get(username=un)
            UO.set_password(pw)
            UO.save()
            return HttpResponse('Password Changed SuccessFully')
        else:
            return HttpResponse('OTP Not Matched')
    
    return render(request,'OtpPage.html')
    




    


    
    
    



    