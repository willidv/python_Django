# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from models import *

from django.contrib import messages



# Create your views here.
def index(request):
    return render(request, "login/login.html")

def add(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect(index)

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name =  request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        User.objects.create(first_name = first_name, last_name = last_name, email = email, password = password, confirm_password =  confirm_password)
    return render(request, "login/add.html")

def login(request):
    error = User.objects.login_validator(request.POST)
    if len(error):
        for e in error:
            messages.error(request, e)
        return redirect(index)
    else:
        return render(request, "login/add.html")         