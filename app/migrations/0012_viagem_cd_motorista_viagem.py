# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_notificacaoocorrencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='viagem',
            name='cd_motorista_viagem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Motorista'),
        ),
    ]