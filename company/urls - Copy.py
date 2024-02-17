from django.contrib import admin
from django.urls import path
from django.urls import path,include
from . import views

urlpatterns = [
    path('company/',views.company,name='company'),
    path('company/company_register/',views.company_register,name='company_register'),
    path('company/job_offer/',views.create_job_offer,name='create_job_offer'),
    path('company/student_list/',views.student_list,name='student_list'),
    path('company/offer_created/',views.offer_created,name='offer_created'),
    
    
    
]