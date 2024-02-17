from django.contrib import admin
from django.urls import path
from django.urls import path,include
from . import views

urlpatterns = [
    path('student/',views.student ,name='student'),
    path('slogin/',views.slogin ,name='slogin'),
    path('sregister/',views.sregister,name='sregister' ),
    path('success_page/',views.success_page,name='success_page'),
]
