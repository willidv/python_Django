# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    response = "testing testing 1 2"
    return HttpResponse(response)

def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"
        print "*"*50
        return redirect('/')
    else:
        return redirect('/')
    