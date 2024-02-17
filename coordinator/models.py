from django.db import models
 #Create your models here.
class Cdetails(models.Model):
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    password=models.IntegerField()
    
