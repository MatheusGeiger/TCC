# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_viagem_cd_motorista_viagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='status_ocorrencia',
            field=models.CharField(choices=[(b'finalizada', b'Finalizada'), (b'em_andamento', b'Em Andamento'), (b'nao_iniciada', b'Nao Iniciada')], default=b'nao_iniciada', max_length=64),
        ),
    ]
