# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages

from models import *

# fr

# Create your views here.
def index(request):
    return render(request, "course/course.html")

def add(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        Course.objects.create(name = name, description = description)

    courses = Course.objects.all()


    context = {
        "courses" : courses
    }
    return render(request, "course/course.html", context )
    
def remove(request, id):
    course = Course.objects.filter(id = id)
    course.delete()
    return redirect(add)