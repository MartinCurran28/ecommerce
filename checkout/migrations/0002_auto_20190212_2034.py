# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-12 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='county',
            field=models.CharField(max_length=40),
        ),
    ]
