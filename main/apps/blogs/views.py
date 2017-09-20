# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)
def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)
def create(request):
    return redirect('/blogs')
# def show(request):
#     response = "placeholder to display blog " + {{n}}
#     return HttpResponse(response)
def context(request):
    context ={
        "email" : "thisemail@email.com",
        "name" : "Jamaican Dave"
    }
    return render(request, "blogs/blogs.html", context)