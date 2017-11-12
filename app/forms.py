from django import forms
from .models import *

class AddViagem(forms.ModelForm):
    """docstring for AddViagem."""

    class Meta:
        model = Viagem
        fields = ('destino_viagem','cd_motorista_viagem' )
        name = 'Viagem'
        # fields = ('origem_viagem' ,'destino_viagem' ,'data_inicio_viagem' ,'data_fim_viagem' ,'status_ocorrencia' ,'status_viagem','cd_motorista_viagem' )

class AddMotorista(forms.ModelForm):
    """docstring for AddViagem."""

    class Meta:
        model = Motorista
        fields = ('nome_motorista','cpf_motorista','placa_veiculo')
        name = 'Motorista'


class AddVeiculo(forms.ModelForm):
    """docstring for AddViagem."""

    class Meta:
        model = Veiculo
        fields = ('placa_veiculo', 'cor_veiculo', 'modelo_veiculo', 'marca_veiculo', 'ano_veiculo')
        name = 'Veiculo'
