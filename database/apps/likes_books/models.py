# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        user_info = str(self.first_name) + " " + str(self.last_name) + " " + str(self.email) 
        return user_info

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length= 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name = "books")
    liked = models.ManyToManyField(User, related_name="liked_books")

    def __str__(self):
        book_info = str(self.name) + " " + str(self.desc) 
        return book_info
