# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0029_remove_spec_date_submitted'),
    ]

    operations = [
        migrations.AddField(
            model_name='spec',
            name='build',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date was built'),
        ),
    ]
