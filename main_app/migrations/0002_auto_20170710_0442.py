# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('recipe', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Treasure',
        ),
    ]
