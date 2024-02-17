from django.shortcuts import render
from .models import Sregister
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import auth

# Create your views here.
def student(request):
    return render(request,'student.html')
def slogin(request):
    if request.method=='POST':
        usn=request.POST.get('usn')
        password=request.POST.get('password')
        if Sregister.objects.filter(password=password,usn=usn).exists():
            usn="welcome"+usn
            messages.info(request,usn)
            return render(request,'studentpage.html')
        else:
            up=str(usn)+str(password)
            messages.info(request,up)
            return render(request,'login_fail.html')
    else:
            return render(request,'student.html')
        
       
def success_page(request):
    return render(request,'registration_success.html')        
    
def sregister(request):
    if request.method=='POST':
        #entered data is to be fetched and to be stored in DB
        name=request.POST.get('name') 
        usn=request.POST.get('usn') 
        branch=request.POST.get('branch') 
        sem=request.POST.get('sem') 
        phone=request.POST.get('phone') 
        skills=request.POST.get('skills') 
        password=request.POST.get('password') 
        cgpa=request.POST.get('cgpa')
        Sregister.objects.create(name=name, usn=usn,branch=branch,sem=sem,phone=phone,skills=skills,password=password,cgpa=cgpa)
        return redirect('success_page')
    else:
        return render(request,'sregister.html')
        