from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return  render(request, 'safety/pages/home.html', status=201, context={
        'name': 'Fernando Programador',
        'idade': 41,
        'profissao':'Engenheiro de Software'
            })

