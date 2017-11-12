# encoding: utf-8
from django.contrib import admin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import requests
import simplejson
import datetime
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    if request.user.is_authenticated():
        return render(request, 'index_viagem.html', {'viagem' : viagem})
    else:
        return HttpResponseRedirect('/login/?next=%s' % request.path)

def lista_ocorrencia(request):
    if request.user.is_authenticated():
        ocorrencia = Ocorrencia.objects.all()
        return render(request, 'index_ocorrencia.html', {'ocorrencia' : ocorrencia})
    else:
        return HttpResponseRedirect('/login/?next=%s' % request.path)

def ocorrencia(request):
    return render(request, 'index_ocorrencia.html')

def insere_ocorrencia(request,id_viagem,local_ocorrencia):
    viagem = Viagem.objects.get(cd_viagem=id_viagem)
    if viagem.status_viagem == 'nao_iniciada':
        msg='ocorrencia nao registrada, viagem nao iniciada'
        return HttpResponse(msg)
    else:
        ocorrencia = Ocorrencia()
        import ipdb; ipdb.set_trace()
        ocorrencia.id_viagem = id_viagem
        ocorrencia.local_ocorrencia = local_ocorrencia
        ocorrencia.data_ocorrencia = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ocorrencia.save()
        viagem = Viagem.objects.get(cd_viagem=id_viagem)
        viagem.status_ocorrencia = True
        viagem.save()
        msg='ocorrencia registrada'
        return HttpResponse(msg)

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

def lista_viagem(request):
    if request.user.is_authenticated():
        viagem = Viagem.objects.all()
        return render(request, 'index_viagem.html', {'viagem' : viagem})
    else:
        return HttpResponseRedirect('/login/?next=%s' % request.path)

def add_viagem(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = AddViagem(request.POST)
            if form.is_valid():
                viagem = form.save(commit=False)
                viagem.save()
                return redirect('/viagem/%s' % viagem.pk)
        else:
            form = AddViagem()
    else:
        return HttpResponseRedirect('/login/?next=%s' % request.path)
    return render(request, 'add.html', {'form': form})

def lista_motorista(request):
    if request.user.is_authenticated():
        motorista = Motorista.objects.all()
        return render(request, 'index_motorista.html', {'motorista' : motorista})
    else:
        return HttpResponseRedirect('/login/?next=%s' % request.path)

def add_motorista(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = AddMotorista(request.POST)
            if form.is_valid():
                motorista = form.save(commit=False)
                motorista.save()
                return redirect('/lista_motorista')
        else:
            form = AddMotorista()
    else:
        return HttpResponseRedirect('/login/?next=%s' % request.path)
    return render(request, 'add.html', {'form': form})

def lista_veiculo(request):
    if request.user.is_authenticated():
        veiculo = Veiculo.objects.all()
        return render(request, 'index_veiculo.html', {'veiculo' : veiculo})
    else:
        return HttpResponseRedirect('/login/?next=%s' % request.path)

def add_veiculo(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = AddVeiculo(request.POST)
            if form.is_valid():
                veiculo = form.save(commit=False)
                veiculo.save()
                return redirect('/lista_veiculo')
        else:
            form = AddVeiculo()
    else:
        return HttpResponseRedirect('/login/?next=%s' % request.path)
    return render(request, 'add.html', {'form': form})
