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
        try:
            user = User.objects.get(email = email)
        except User.DoesNotExist:
            user = None
        if user == None:
            error.append("You must be a registered user")
            return error
        if user:
            if user.password != postData['password']:
                error.append("You must use the correct password")
                return error
            else:
                return error
        else:
            error.append("You must be a registered user")
            return error

class User(models.Model):
     first_name = models.CharField(max_length = 255)
     last_name = models.CharField(max_length=255)
     email = models.CharField(max_length=255)
     password = models.CharField(max_length=255)
     confirm_password = models.CharField(max_length=255)
     objects = UserManager()
     
     def __str__(self):
        user_info = str(self.first_name) + " " + str(self.last_name) + " " + str(self.email) 
        return user_info

class Author(models.Model):
    name = models.CharField(max_length = 255)
    
    def __str__(self):
        author_info = str(self.first_name)  + " " + str(self.last_name)
        return author_info

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="book_written")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        book_info = str(self.title) 
        return book_info

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    reviewer = models.ForeignKey(User, related_name="reviews")
    book = models.ForeignKey(Book, related_name="books_review")
    created_at = models.DateTimeField(auto_now_add = True)

