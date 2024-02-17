from django.db import models

# Create your models here.
class Create_job_offer(models.Model):
    name=models.CharField(max_length=50)
    ctc=models.IntegerField()
    cgpa=models.FloatField()
    role=models.CharField(max_length=15)
    deadline=models.DateField(auto_now_add=True)
    
    
    
    
class Company_details(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=15)
    password=models.CharField(max_length=10)
    address=models.TextField(max_length=500)
    
    
    
    
