from django.urls import path
from django.contrib import admin
from safety.views import home

urlpatterns = [
    path('', home),
    
]
