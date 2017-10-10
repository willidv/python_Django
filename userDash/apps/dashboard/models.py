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
            errors.append("First name should be longer than 2 characters")
        if len(postData['last_name']) < 2:
            errors.append('Last name should be longer than 2 characters')
        if not NAMES_REGEX.match(postData['first_name']):
            errors.append("First name must be letters only")
        if not NAMES_REGEX.match(postData['last_name']):
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

        # try:
        #     user = User.objects.get(email = email)
        # except User.DoesNotExist:
        #     user = None
        
        # if user == None:
        #     error.append("You must be a registered user")
        #     return error
        # if user:
        #     if user.password != postData['password']:
        #         error.append("You must use the correct password")
        #         return error
        #     else:
        #         return error
        # else:
        #     error.append("You must be a registered user")
        #     return error
        



class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    admin = models.BooleanField(default = False)
    following = models.ManyToManyField('User', related_name='followers')
    objects = UserManager()

    def __str__(self):
        user_info = str(self.first_name) + " " + str(self.last_name) + " " + str(self.email) 
        return user_info

class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name= "messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "received")



