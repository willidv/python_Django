# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        book_info = str(self.name)
        return book_info

class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name = "authors")
    notes = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)
    

    def __str__(self):
        author_info = str(self.first_name) + " " + str(self.last_name)
        return author_info