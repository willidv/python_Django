# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20171009_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='_user_following_+', to='dashboard.User'),
        ),
    ]
