# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect 
import datetime
print "hello"
  # the index function is called when root is visited
def index(request):
    context = {
        "Date": datetime.date.today(),
        "Time": datetime.datetime.now()
    }
    return render(request, "time_display/time.html", context)
