# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import re

NAMES_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        if len(postData['first_name']) < 2:
            errors.append("First name should be more than 2 characters")
        if len(postData['last_name']) < 2:
            errors.append("Last name should be more than 2 characters")
        if not NAMES_REGEX.match(postData["first_name"]):
            errors.append("Name must be letters only")
        if not NAMES_REGEX.match(postData["last_name"]):
            errors.append("Name must be letters only")
        if not EMAIL_REGEX.match(postData["email"]):
            errors.append("Email must be the correct format")
        if len(postData['password']) < 8:
            errors.append("Password must be longer than 8 characters")
        if postData["password"] != postData["confirm_password"]:
            errors.append("Passwords must match")     
        return errors
    
    def login_validator(self, postData):
        error=[]
        email = postData['email']
        password = postData['password']
        print email
        print password
        user = User.objects.get(email = email)
        if not user.email == postData['email']:
            error.append("You must be a registered user")
        if not user.password == postData['password']:
            error.append("You must use the correct password")

        return error

class User(models.Model):
     first_name = models.CharField(max_length = 255)
     last_name = models.CharField(max_length=255)
     email = models.CharField(max_length=255)
     password = models.CharField(max_length=255)
     confirm_password = models.CharField(max_length=255)
     objects = UserManager()
