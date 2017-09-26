# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from django import forms

# Create your views here.
def index(request):
    # request.session["total_price"] = 0
    request.session["item_price"] = 0
    # request.session["items"] = 0
    return render(request, "amadon_app/amadon_app.html")

def buy(request):
    if request.method == "POST":
        p_id = request.POST['p_id']
        quantity = request.POST['quantity']

        if not "total_price" in request.session:
            total_price = 0
            request.session["total_price"] = 0.0

        if not "item_price" in request.session:
            item_price = 0
            request.session["item_price"] = 0.0

        if not "items" in request.session:
            request.session["items"] = 0.0
               
        if not "my_items" in request.session:
            my_items = []
            request.session['my_items'] = my_items

        item_prices = {
            "Dojo Tshirt" : 19.99,
            "Dojo Sweater" : 29.99,
            "Dojo Cup" : 4.99,
            "Dojo Book" : 49.99
        }

        request.session['my_items'].append(p_id)
        request.session.modified= True

        if request.POST['p_id'] == "1":
            request.session["item_price"] = item_prices["Dojo Tshirt"] * (float(quantity))
            request.session["total_price"] = request.session["total_price"] + (item_prices["Dojo Tshirt"] * (float(quantity)))
            request.session["items"] += (float(quantity))

        elif request.POST['p_id'] == "2": 
            request.session["item_price"] = item_prices["Dojo Sweater"] * (float(quantity))
            request.session["total_price"] = request.session["total_price"] + (item_prices["Dojo Sweater"] * (float(quantity)))
            request.session["items"] += (float(quantity))

        elif request.POST['p_id'] == "3":
            request.session["item_price"] = item_prices["Dojo Cup"] * (float(quantity)) 
            request.session["total_price"] = request.session["total_price"] + (item_prices["Dojo Cup"] * (float(quantity)))
            request.session["items"] += (float(quantity))

        elif request.POST['p_id'] == "4": 
            request.session["item_price"] = item_prices["Dojo Book"] * (float(quantity))
            request.session["total_price"] = request.session["total_price"] + (item_prices["Dojo Book"] * (float(quantity)))
            request.session["items"] += (float(quantity))
        

    return redirect(successful)

def successful(request):
    return render(request, "amadon_app/success.html" )