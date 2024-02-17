from django.db import models


class Sregister(models.Model):
    name=models.CharField(max_length=50)
    usn=models.CharField(max_length=10)
    branch=models.CharField(max_length=10)
    sem=models.IntegerField()
    phone=models.TextField()
    skills=models.TextField()
    password=models.TextField(max_length=10)
    cgpa=models.FloatField()
    
    
    
    
