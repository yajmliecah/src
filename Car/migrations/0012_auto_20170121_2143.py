# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 21:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0011_auto_20170121_1409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='spec',
            options={'ordering': ['-id'], 'verbose_name': 'Spec', 'verbose_name_plural': 'Specs'},
        ),
        migrations.AlterField(
            model_name='spec',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specs', to='Car.Brand', verbose_name='brand'),
        ),
        migrations.AlterField(
            model_name='spec',
            name='date_submitted',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date submitted'),
        ),
        migrations.AlterField(
            model_name='spec',
            name='details',
            field=models.TextField(blank=True, help_text='Enter car details', verbose_name='details'),
        ),
        migrations.AlterField(
            model_name='spec',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='spec',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='spec',
            name='types',
            field=models.CharField(choices=[(b'CAR', b'Car'), (b'MOTORCYCLE', b'MotorCycle'), (b'VEHICLE', b'Vehicle')], max_length=50, verbose_name='type'),
        ),
    ]
