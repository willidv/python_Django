# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

import re

NAMES_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+$')



# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        print postData
        errors = []
        if len(postData['name']) < 2:
            errors.append("Name should be longer than 2 characters")
        if len(postData['alias']) < 2:
            errors.append('Alias should be longer than 2 characters')
        if not NAMES_REGEX.match(postData['name']):
            errors.append("First name must be letters only")
        if not NAMES_REGEX.match(postData['alias']):
            errors.append("Last name must be letters only")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Email must be the correct format")
        if postData['password'] != postData["confirm_password"]:
            errors.append("Passwords must match")
        return errors
    
    def login_validator(self, postData):
        error=[]
        email = postData['email']
        password = postData['password']
        print postData
        try:
            user = User.objects.get(email = email)
        except User.DoesNotExist:
            user = None
        
        if user == None:
            error.append("You must be a registered user")
            return error
        else:
            if user.password != postData['password']:
                error.append("You must use the correct password")
                return error

class User(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()
    def __str__(self):
        user_info = str(self.name) + " " + str(self.alias) + " " + str(self.email) 
        return user_info

class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=255)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "left")
    fan = models.ManyToManyField(User, related_name= "favorite_quotes")
