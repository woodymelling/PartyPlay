# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-05 01:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PartyPlay', '0023_auto_20171004_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='room',
        ),
    ]
