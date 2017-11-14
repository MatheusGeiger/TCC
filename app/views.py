# -*- coding:utf-8 -*-
from django.contrib import admin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .controllers import *
import requests
import simplejson
import datetime
from django.http import HttpResponseRedirect
from django.contrib import messages

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

def insere_ocorrencia(request, id_viagem, latitude, longitude):
    viagem = Viagem.objects.get(cd_viagem=id_viagem)
    if viagem.status_viagem == 'nao_iniciada':
        msg='ocorrencia nao registrada, viagem nao iniciada'
        return False
    else:
        local_ocorrencia = ControlerGetAddress(latitude,longitude)
        ocorrencia = Ocorrencia()
        ocorrencia.cd_viagem_id = id_viagem
        ocorrencia.local_ocorrencia = local_ocorrencia
        ocorrencia.ds_ocorrencia = 'Porta aberta'
        ocorrencia.data_ocorrencia = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ocorrencia.save()
        viagem = Viagem.objects.get(cd_viagem=id_viagem)
        viagem.status_ocorrencia = True
        viagem.save()
        msg='ocorrencia registrada'
        return True

def iniciar_viagem(request,id_viagem,latitude,longitude):
    viagem = Viagem.objects.all().filter(status_viagem='em_andamento')
    if (viagem.count() >= 1) :
        messages.error(request, 'Ops ! Temos uma outra viagem em andamento...')
        return HttpResponseRedirect('/viagem/%s' % id_viagem)
    else:
        address_origem = ControlerGetAddress(latitude,longitude)
        viagem = Viagem.objects.get(cd_viagem=id_viagem)
        viagem.origem_viagem = address_origem
        viagem.status_viagem = 'em_andamento'
        viagem.data_inicio_viagem = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        viagem.save()
        messages.success(request, 'Viagem Iniciada. ')
    return HttpResponseRedirect('/viagem/%s' % id_viagem)

def finalizar_viagem(request,id_viagem,latitude,longitude):
    viagem = Viagem.objects.get(cd_viagem=id_viagem)
    destino = viagem.destino_viagem
    distancia_valida = ControlerGetDistance(destino,latitude,longitude)
    if type(distancia_valida) == str:
        messages.error(request, 'Não foi possivel localizar o endereco de Origem')
        return HttpResponseRedirect('/viagem/%s' % id_viagem)
    else:
        if distancia_valida:
            viagem.status_viagem = 'finalizada'
            viagem.data_fim_viagem = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            viagem.save()
            messages.success(request, 'Viagem Finalizada. ')
            return HttpResponseRedirect('/viagem/%s' % id_viagem)
        else:
            messages.error(request, 'Não foi possivel finalizar a Viagem, caminhão não chegou ao destino')
            return HttpResponseRedirect('/viagem/%s' % id_viagem)

def insere_coordenada(request,latitude,longitude,status_porta):
    try:
        viagem = Viagem.objects.filter(status_viagem='em_andamento').get()
    except:
        return HttpResponse(status=204)

    coordenada = CoordenadasVeiculo()
    coordenada.latitude = latitude
    coordenada.longitude = longitude

    if int(status_porta) == 0:
        coordenada.porta_aberta = False
        coordenada.cd_viagem_id = viagem.pk
        coordenada.save()
    else:
        coordenada.porta_aberta = True
        coordenada.cd_viagem_id= viagem.pk
        coordenada.save()
        id_viagem = viagem.pk
        insere_ocorrencia(request,id_viagem,latitude,longitude)
    return HttpResponse(status=200)


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

def cancelar_viagem(request,id_viagem):
    if request.user.is_authenticated():
        viagem = Viagem.objects.get(cd_viagem=id_viagem)
        viagem.status_viagem = 'cancelada'
        viagem.data_fim_viagem = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        viagem.save()
        messages.success(request, 'Viagem Cancelada. ')
        return HttpResponseRedirect('/viagem/%s' % id_viagem)
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
