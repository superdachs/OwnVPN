# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-11 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openvpn', '0003_auto_20161011_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='openvpnclient',
            name='server_port',
            field=models.IntegerField(default=1194),
        ),
        migrations.AlterField(
            model_name='openvpnclient',
            name='port',
            field=models.IntegerField(unique=True),
        ),
        migrations.RemoveField(
            model_name='openvpnclient',
            name='local_port',
        ),
        migrations.AlterUniqueTogether(
            name='openvpnclient',
            unique_together=set([('gateway', 'server_port')]),
        ),
    ]
