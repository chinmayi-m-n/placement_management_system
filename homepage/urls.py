from django.contrib import admin
from django.urls import path
from django.urls import path,include
from  . import views

urlpatterns = [
    path('',views.home),
    path('student/',views.student),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_registration/',views.admin_registration),
    
]
