# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0002_auto_20170923_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
