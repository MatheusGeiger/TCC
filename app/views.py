from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import requests
# Create your views here.

def index(request):
    return render(request, 'index.html')

def viagem(request):
    return render(request, 'index_viagem.html')

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})
