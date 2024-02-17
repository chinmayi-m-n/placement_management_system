from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def student(request):
    return render(request,'student.html')
def admin_login(request):
    return render(request,'admin_login.html')
def admin_registration(request):
    return render(request,'admin_register.html')