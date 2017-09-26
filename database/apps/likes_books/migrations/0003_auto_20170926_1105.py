# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('likes_books', '0002_auto_20170926_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='likes_books.User'),
        ),
    ]