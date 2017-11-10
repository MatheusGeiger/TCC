# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20171107_0111'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Greeting',
        ),
        migrations.AlterField(
            model_name='viagem',
            name='status_viagem',
            field=models.CharField(choices=[(b'nao_iniciada', b'Nao Iniciada'), (b'finalizada', b'Finalizada'), (b'em_andamento', b'Em Andamento')], default=b'nao_iniciada', max_length=64),
        ),
    ]
