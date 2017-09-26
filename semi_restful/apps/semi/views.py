# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from models import *

# Create your views here.
def index(request):
    return render(request, "semi/semi.html", {"users": User.objects.all() })

def add(request):
    return render(request, "semi/add.html")

def make(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name =  request.POST["last_name"]
        email=request.POST["email"]
        User.objects.create(first_name = first_name, last_name = last_name, email = email)
    return redirect(index)

def edit(request, id):
    return render(request, "semi/edit.html", {"user": User.objects.get(id=id) })

def show(request, id):
    return render(request, "semi/show.html", {"user": User.objects.get(id=id) })

def update(request, id):
    if request.method == "POST":
        user = User.objects.get(id = id)
        user.first_name = request.POST['first_name'] 
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
    return redirect(index)

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect(index)
    