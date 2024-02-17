from django.http import HttpResponse
from django.shortcuts import render
from .models import Company_details
from django.contrib import messages
from .models import Create_job_offer
from student.models import Sregister
def company(request):
    if request.method=='POST':
        name=request.POST.get('comp_name')
        password=request.POST.get('password')
        if Company_details.objects.filter(name=name,password=password).exists():
            msg="welcome: "+name
            messages.info(request,msg)
            return render(request,'company_page.html')
        else:
            messages.info(request,"INVALID CREDENTIALS")
            return render(request,'company_login_status.html')
        
        
        
    else:
        return render(request,'company_login.html')
    
def company_register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        address=request.POST.get('address')
        details=Company_details.objects.create(name=name,email=email,password=password,address=address)
        if details:
            messages.info(request,"PROVIDED DETAILS REGISTERED SUCCESSFULLY")
            return render(request,'company_login_status.html')
        else:
            messages.info(request,"UNABLE TO REGISTER TRY AGAIN")
            return render(request,'company_register.html')
            
        
    return render(request,'company_register.html')
def create_job_offer(request):
    if request.method=='POST':
        name=request.POST.get('name')
        ctc=request.POST.get('ctc')
        deadline=request.POST.get('deadline')
        role=request.POST.get('role')
        cgpa=request.POST.get('cgpa')
        Create_job_offer.objects.create(name=name,ctc=ctc,cgpa=cgpa,role=role,deadline=deadline,)
        messages.info(request,"job profile created successfully")
        return render(request,'company_login_status.html')
    else:
        return render(request,'create_job_offer.html')

def student_list(request):
    cutoff_cgpa=request.POST.get('cgpa_cutoff')
    if cutoff_cgpa is None or cutoff_cgpa == '':
        return HttpResponse("CGPA cutoff is not provided.")
    else:
        st_rows=Sregister.objects.filter(cgpa__gte=cutoff_cgpa)
        st_list=[]
        for row in st_rows:
            st_list.extend([row.name,row.usn,row.branch,row.sem,row.cgpa,row.skills])
        return render(request,'student_list.html',{'st_list':st_list})
        
    
def offer_created(request):
    name=request.POST.get('name')
    ctc=request.POST.get('ctc')
    cgpa=request.POST.get('cgpa')
    role=request.POST.get('role')
    deadline=request.POST.get('deadline')
    Create_job_offer.objects.create(name=name,ctc=ctc,cgpa=cgpa,role=role,deadline=deadline)
    messages.info(request,"job offer created successfully")
    return render(request,'company_login_status.html')
    
    
    
    
    
    
    messages.info(request,"job offer created successfully")
    return render(request,'company_login_status.html')
        
        
        
        
        
        
    
    
    
    
              