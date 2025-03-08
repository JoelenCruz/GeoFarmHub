from . import views
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect, render



urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")), 
    path('', lambda request: redirect('initial')),
    path('initial/', views.initial, name='initial'),
]
