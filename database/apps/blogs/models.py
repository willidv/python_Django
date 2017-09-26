# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        blog_info = str(self.name) + " " + str(self.desc)
        return blog_info

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    blog = models.ForeignKey(Blog, related_name = "comments")

    def __str__(self):
        the_comment = str(self.comment)
        return the_comment

class Admin(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    blogs = models.ManyToManyField(Blog, related_name= "admins")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        info = str(self.first_name) + " " + str(self.last_name)
        return info 