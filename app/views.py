from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import requests
import simplejson

# Create your views here.

def index(request):
    return render(request, 'index_viagem.html')

def viagem(request,id_viagem):
    viagem = Viagem.objects.get(cd_viagem=id_viagem)
    return render(request, 'viagem.html', {'viagem' : viagem})

def ocorrencia(request):
    return render(request, 'index_ocorrencia.html')

def lista_viagem(request):
    viagem = Viagem.objects.all()
    return render(request, 'index_viagem.html', {'viagem' : viagem})

def lista_ocorrencia(request):
    ocorrencia = Ocorrencia.objects.all()
    return render(request, 'index_ocorrencia.html', {'ocorrencia' : ocorrencia})

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})
