# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='name', max_length=255),
            preserve_default=False,
        ),
    ]
