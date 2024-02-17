from django.shortcuts import render
from .models import Cdetails
from django.contrib import messages


# Create your views here.
def coordinator_register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        register=Cdetails.objects.create(name=name,email=email,phone=phone,password=password)
        if register:
            return render(request,'coordinator_login.html')
        else:
            pass
    else:
        return render(request,'coordinator_register.html')
        
def coordinator_login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        if Cdetails.objects.filter(name=name,password=password).exists():
            msg="WELCOME: "+name
            messages.info(request,msg)
            return render(request,'coordinator_page.html')
        else:
            messages.info(request,"INVALID CREDENTIALS")
            return render(request,'coordinator_login_fail.html')
        
        

    else:
        return render(request,'coordinator_login.html')
    
    
    
