# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse 

from django import forms

# Create your views here.
def index(request):
    
    return render(request, "words/words.html")

def add(request):
    if request.method == 'POST':
        if request.POST.get('checkBox', False):
            checked = True
        else:
            checked = False

        if not request.session['my_words']:
            my_words = []
            request.session['my_words'] = my_words
        words_to_add = {
            "word" : request.POST['word'],
            "color" : request.POST['color'],
            "checkbox" : checked
        }        
        request.session['my_words'].append(words_to_add)
        request.session.modified= True
        print request.session['my_words']
        print request.POST
    
    return redirect(index)

def clear(request):
   request.session['my_words'] = []
   return redirect(index)