from . import views
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect, render
from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, FarmViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'farms', FarmViewSet)
router.register(r'transactions', TransactionViewSet)



urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")), 
    path('', lambda request: redirect('initial')),
    path('initial/', views.initial, name='initial'),
]
