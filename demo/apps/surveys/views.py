# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, "surveys/surveys.html")

def filled(request):
    request.session['number'] = 0
    number = request.session['number']
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comments'] = request.POST['comments']
    context = {
        "number" : number,
        "name" : request.session['name'],
        "location" : request.session['location'],
        "language" : request.session['language'],
        "comments" : request.session['comments']    
    }
    if request.method == "POST":
        number += 1
    return redirect(success)

def success(request):
    return render(request, "surveys/forms.html")
