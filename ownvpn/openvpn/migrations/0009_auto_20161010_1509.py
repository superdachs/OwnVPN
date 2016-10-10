# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openvpn', '0008_auto_20161010_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openvpnserver',
            name='static_key',
            field=models.TextField(default='#\n# 2048 bit OpenVPN static key\n#\n-----BEGIN OpenVPN Static key V1-----\ncc5bec28edac56810981b27bab5b17c1\nf0b693b36f24ed62822dc9f8d8e39c46\n4df85ed684aa0172361f7a1133210431\n06c3ad58c523144069f4ce018bb0ab5b\n7b4e7a985bd4fdd6dbcdaa184981d90b\nbba67f57f91519b9c5f900d5f902b4d7\n834af068af56b5c84133bd9178e52219\n293c8271290a5617e42db4dee8c9e668\n910551a4c2c9af4d838f2b721f42501a\nd57d0d3e37ae2765b1371b0c70748675\n61f043dac0cc7644d86bc8601df66bc9\n1f2b905d2a10f35065d920d6efc99b6f\n786a015ba31e7fb2c92e09ac001db5e2\n209a0c4025afd1f81ef71948908936f8\ne12f254d6f13b95fd5e57ffac751407c\n1a4e966f413b777aacf653bfd9638188\n-----END OpenVPN Static key V1-----\n'),
        ),
    ]