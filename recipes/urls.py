from django.urls import path
from django.contrib import admin
from recipes.views import home, contato, sobre

urlpatterns = [
    path('recipes/', home),
    path('recipes/contato/', contato),
    path('recipes/sobre/', sobre),

    
]
