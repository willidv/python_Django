# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 22:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninjas',
            name='Dojos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ninjas', to='dojo_ninjas.Dojos'),
        ),
    ]