from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('coordinator/',views.coordinator_login,name='coordinator_login'),
    path('coordinator/coordinator_register/',views.coordinator_register,name='coordinator_register'),
]

