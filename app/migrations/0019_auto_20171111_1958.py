# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20171111_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='marca_veiculo',
            field=models.CharField(choices=[(b'Mercedes-Benz', b'Mercedes-Benz'), (b'MAN (VW)', b'MAN (VW)'), (b'Ford Caminhoes', b'Ford Caminhoes'), (b'Volvo', b'Volvo')], max_length=64),
        ),
    ]
