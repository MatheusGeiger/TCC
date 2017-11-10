# encoding: utf-8
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import requests
import simplejson
from django.http import HttpResponseRedirect


# Create your views here.

def index(request):
    if request.user.is_authenticated():
        return render(request, 'index_viagem.html', {'viagem' : viagem})
    else:
        return HttpResponseRedirect('/login/?next=%s' % request.path)

def viagem(request,id_viagem):
    if request.user.is_authenticated():
        viagem = Viagem.objects.get(cd_viagem=id_viagem)
        ocorrencia = Ocorrencia.objects.all().filter(cd_viagem=id_viagem)
        lista = ocorrencia.values_list()
        location = [{'location': lista[2].encode('utf8')} for lista in lista]
        context = {
            'viagem' : viagem,
            'ocorrencia' : ocorrencia,
            'location' : location
        }
        return render(request, 'viagem.html', context)
    else:
        return HttpResponseRedirect('/login/?next=%s' % request.path)


def ocorrencia(request):
    return render(request, 'index_ocorrencia.html')

def lista_viagem(request):
    if request.user.is_authenticated():
        viagem = Viagem.objects.all()
        return render(request, 'index_viagem.html', {'viagem' : viagem})
    else:
        return HttpResponseRedirect('/login/?next=%s' % request.path)

def lista_ocorrencia(request):
    if request.user.is_authenticated():
        ocorrencia = Ocorrencia.objects.all()
        return render(request, 'index_ocorrencia.html', {'ocorrencia' : ocorrencia})
    else:
        return HttpResponseRedirect('/login/?next=%s' % request.path)
