# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 18:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20171105_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificacaoOcorrencia',
            fields=[
                ('cd_notificacao_ocorrencia', models.AutoField(primary_key=True, serialize=False)),
                ('cd_ocorrencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Ocorrencia')),
            ],
            options={
                'verbose_name': 'Notificacao',
                'verbose_name_plural': 'Notificacoes',
            },
        ),
    ]
