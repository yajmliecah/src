# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0009_auto_20170121_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='new',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='condition',
            name='used',
            field=models.BooleanField(),
        ),
    ]
