# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20171111_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='origem_viagem',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
