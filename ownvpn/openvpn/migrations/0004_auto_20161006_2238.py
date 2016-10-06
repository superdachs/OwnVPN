# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-06 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openvpn', '0003_auto_20161006_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='openvpn',
            name='static_key',
        ),
        migrations.AddField(
            model_name='openvpnclient',
            name='static_key',
            field=models.TextField(default='vla'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='openvpnserver',
            name='static_key',
            field=models.TextField(default='bla'),
            preserve_default=False,
        ),
    ]