# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20171105_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='cd_ocorrencia',
            field=models.ManyToManyField(blank=True, null=True, to='app.Ocorrencia'),
        ),
    ]
