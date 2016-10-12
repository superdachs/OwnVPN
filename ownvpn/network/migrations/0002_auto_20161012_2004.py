# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-12 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='dev_name',
            field=models.CharField(choices=[('eth0', 'eth0'), ('enp0s8', 'enp0s8')], max_length=10, unique=True),
        ),
    ]
