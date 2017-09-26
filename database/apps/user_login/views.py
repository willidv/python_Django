# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from models import *

from django import forms
# Create your views here.

def index(request):
    response = "virginia is my wife"
    return HttpResponse(response)