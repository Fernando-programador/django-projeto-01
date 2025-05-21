from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return  render(request, 'home.html', status=200, context={
        'name': 'Fernando Correa',
        'idade': 42,
        'sexo': 'masculino'
    })

def sobre(request):
    return HttpResponse('ESTOU NA PAGINA SOBRE')

def contato(request):
    return HttpResponse('ESTOU NA PAGINA CONTATO')
