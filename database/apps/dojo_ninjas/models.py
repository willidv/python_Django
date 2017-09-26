# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(null=True)

    def __str__(self):
        info = str(self.name) + " " + str(self.city) + " " + str(self.state)
        return info

class Ninjas(models.Model):
    Dojos = models.ForeignKey(Dojos, related_name = "Ninjas")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        ninja_info = str(self.first_name) + " " + str(self.last_name)
        return ninja_info
