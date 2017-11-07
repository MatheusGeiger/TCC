from django.contrib import admin
from .models import *
# Register your models here.

class VeiculoAdmin(admin.ModelAdmin):

    list_display = (
        'placa_veiculo',
        'cor_veiculo',
        'modelo_veiculo',
        'marca_veiculo',
        'ano_veiculo'
    )
    search_fields = [
        'placa_veiculo',
        'cor_veiculo',
        'modelo_veiculo',
        'marca_veiculo',
        'ano_veiculo'
    ]

class MotoristaAdmin(admin.ModelAdmin):

    list_display = (
        'cd_motorista',
        'nome_motorista',
        'cpf_motorista',
        'placa_veiculo'
    )
    search_fields = [
        'cd_motorista',
        'nome_motorista',
        'cpf_motorista',
        'placa_veiculo'
    ]

class OcorrenciaAdmin(admin.ModelAdmin):

    list_display = (
        'cd_ocorrencia',
        'ds_ocorrencia',
        'local_ocorrencia',
        'data_ocorrencia'
    )
    search_fields = [
        'cd_ocorrencia',
        'ds_ocorrencia',
        'local_ocorrencia',
        'data_ocorrencia'
    ]

class ViagemAdmin(admin.ModelAdmin):

    list_display = (
        'cd_viagem',
        'origem_viagem',
        'destino_viagem',
        'data_inicio_viagem',
        'data_fim_viagem',
        'cd_motorista_viagem'
    )
    search_fields = [
        'cd_viagem',
        'origem_viagem',
        'destino_viagem',
        'data_inicio_viagem',
        'data_fim_viagem'
    ]

class NotificacaoOcorrenciaAdmin(admin.ModelAdmin):

    list_display = (
        'cd_notificacao_ocorrencia',
        'cd_ocorrencia'
    )
    search_fields = [
        'cd_notificacao_ocorrencia',
        'cd_ocorrencia'
    ]

admin.site.register(Veiculo, VeiculoAdmin)
admin.site.register(Motorista, MotoristaAdmin)
admin.site.register(Ocorrencia, OcorrenciaAdmin)
admin.site.register(Viagem, ViagemAdmin)
admin.site.register(NotificacaoOcorrencia, NotificacaoOcorrenciaAdmin)
