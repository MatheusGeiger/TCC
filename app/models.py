from django.db import models

class Veiculo(models.Model):

    placa_veiculo = models.CharField(
        max_length=8,
        primary_key=True
    )
    cor_veiculo = models.CharField(
        max_length=10
    )
    modelo_veiculo = models.CharField(
        max_length=50
    )
    marca_veiculo = models.CharField(
        max_length=64,
        choices=(
            ('Mercedes-Benz','Mercedes-Benz'),
            ('MAN (VW)','MAN (VW)'),
            ('Ford Caminhoes','Ford Caminhoes'),
            ('Volvo','Volvo')
        )
    )
    ano_veiculo = models.CharField(
        max_length=4,
        choices= (
            ('2007','2007'),
            ('2008','2008'),
            ('2009','2009'),
            ('2010','2010'),
            ('2011','2011'),
            ('2012','2012'),
            ('2013','2013'),
            ('2014','2014'),
            ('2015','2015'),
            ('2016','2016'),
            ('2017','2017'),
            ('2018','2018')
        )
    )

    def __unicode__(self):
        return self.placa_veiculo or ''

    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'

class Motorista(models.Model):

    cd_motorista = models.AutoField(
        primary_key=True
    )
    nome_motorista = models.CharField(
        max_length=50
    )
    cpf_motorista = models.CharField(
        max_length=14
    )
    placa_veiculo = models.ForeignKey(
        Veiculo,
        null=False,
        blank=False
    )

    def __unicode__(self):
        return self.nome_motorista or ''

    class Meta:
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'

class Viagem(models.Model):

    cd_viagem = models.AutoField(
        primary_key=True
    )
    origem_viagem = models.CharField(
        max_length=100
    )
    destino_viagem = models.CharField(
        max_length=100
    )
    data_inicio_viagem = models.DateTimeField(
        null=True,
        blank=True
    )
    data_fim_viagem = models.DateTimeField(
        null=True,
        blank=True
    )
    status_ocorrencia = models.BooleanField(default=False)
    status_viagem = models.CharField(
        max_length=64,
        choices=(
            ('nao_iniciada', 'Nao Iniciada'),
            ('finalizada', 'Finalizada'),
            ('em_andamento', 'Em Andamento')
        ),
        default='nao_iniciada'
    )
    cd_motorista_viagem = models.ForeignKey(
        Motorista,
        null=True,
        blank=True
    )

    def __unicode__(self):
        return str(self.cd_viagem) or ''

    class Meta:
        verbose_name = 'Viagem'
        verbose_name_plural = 'Viagens'

class Ocorrencia(models.Model):

    cd_ocorrencia = models.AutoField(
        primary_key=True
    )
    ds_ocorrencia = models.CharField(
        max_length=100
    )
    local_ocorrencia = models.CharField(
        max_length=100
    )
    data_ocorrencia = models.DateTimeField(
        null=True,
        blank=True
    )
    cd_viagem = models.ForeignKey(
        Viagem,
        null=True,
        blank=True
    )

    def __unicode__(self):
        return str(self.cd_ocorrencia) or ''

    class Meta:
        verbose_name = 'Ocorrencia'
        verbose_name_plural = 'Ocorrencias'

class NotificacaoOcorrencia(models.Model):

    cd_notificacao_ocorrencia = models.AutoField(
        primary_key=True
    )
    cd_ocorrencia = models.ForeignKey(
        Ocorrencia,
        null=False,
        blank=False
    )

    def __unicode__(self):
        return str(self.cd_notificacao_ocorrencia) or ''

    class Meta:
        verbose_name = 'Notificacao'
        verbose_name_plural = 'Notificacoes'
