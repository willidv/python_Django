# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pbelt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField()),
                ('author', models.CharField(max_length=255)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted', to='pbelt.User')),
            ],
        ),
    ]
