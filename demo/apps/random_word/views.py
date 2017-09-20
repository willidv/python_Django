# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    word = get_random_string(length=14)
    context = {
        "number" : request.session['counter'],
        "word" : word
    }
    if request.method == "POST":
        request.session['counter'] = 0
        request.session['counter'] += 1
        word = get_random_string(length=14)
    return render(request, "random_word/random_word.html", context)