# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0026_auto_20170125_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spec',
            name='date_submitted',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='date submitted'),
        ),
    ]
