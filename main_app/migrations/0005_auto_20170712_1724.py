# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_ipod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='entry',
            field=models.CharField(max_length=1000),
        ),
    ]
