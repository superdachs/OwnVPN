# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-10 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openvpn', '0007_auto_20161007_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openvpnserver',
            name='static_key',
            field=models.TextField(default='#\n# 2048 bit OpenVPN static key\n#\n-----BEGIN OpenVPN Static key V1-----\ndb6b3a0bfd2d5ea68cc230c67ee0699c\n7fbe1c14b33cfe218364be335a1f73bc\nc0516524c8fa326afeab0ef1359bb1ff\n0ad8daaaf627a5788040e51ff63cd97b\n3899ac1abc32dad0596bc3034cbb942b\n23c14290c2975b9d3e5f68cb08f38d10\n438ea9393f346878b007ece62b8dbfd7\nbe2571752f2270196cee429741dd463c\nf932ba35bd3b82e7dc093c9ffe98dc0d\n32917e659b76816d3a349f5d00df5934\n80d6d3f7846ceb4e9e48240449d69197\n87c786d7d3eb717d27cbf0515d148c10\n1d189ada10977fc866b711a519118172\n3729b4c235351bea5122dc19d1d1dfa7\nd5dc9bd4e23e030d2cf8d072a83411d7\n6f1165a04bd1e7e1958c1c5c156ed8da\n-----END OpenVPN Static key V1-----\n'),
        ),
    ]