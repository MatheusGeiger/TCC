# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20171105_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViagemOcorrencia',
            fields=[
                ('cd_viagem_ocorrencia', models.AutoField(primary_key=True, serialize=False)),
                ('cd_ocorrencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Ocorrencia')),
            ],
            options={
                'verbose_name': 'Viagem Ocorrencia',
                'verbose_name_plural': 'Viagem e Ocorrencias',
            },
        ),
        migrations.RemoveField(
            model_name='viagem',
            name='cd_ocorrencia',
        ),
        migrations.AddField(
            model_name='viagem',
            name='status_ocorrencia',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='status_viagem',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='viagemocorrencia',
            name='cd_viagem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Viagem'),
        ),
    ]