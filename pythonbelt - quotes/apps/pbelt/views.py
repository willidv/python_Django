# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from models import * 

from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "pbelt/register.html")


def register(request):
    
    errors = User.objects.basic_validator(request.POST)
   
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect(index)
    
    if request.method == "POST":
        name = request.POST['name']
        alias = request.POST['alias']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        user = User.objects.create(name = request.POST['name'], alias= alias , email = email, password = password)
        user.save()
        
        request.session['id'] = user.id
        users = User.objects.all()

        context = {
            "users" : users,  
        }
        return redirect("/home")


def login(request):
    error = User.objects.login_validator(request.POST)
    
    if type(error) == list:
        for e in error:
            messages.error(request, e)
        return redirect(index)
    else:
        email = request.POST['email']
        user = User.objects.get(email = email)

        if id not in  request.session:
            request.session['id'] = user.id

        else:
            return redirect("/index")
            

        
        users = User.objects.all()
        context = {
            "users" : users  
        }

        return redirect("/home")

def home(request):
    users = User.objects.all()
    quotes = Quote.objects.all()
    
    thisuser = User.objects.get(id = request.session['id'])
    fav_quotes = Quote.objects.filter(fan = thisuser)
    their_quotes = Quote.objects.filter(posted_by = thisuser)


    context = {
            "thisuser" : thisuser,
            "quotes" : quotes,
            "fav_quotes" : fav_quotes   
        }
    return render(request, "pbelt/home.html", context)

def quote(request):
    user = User.objects.get(id = request.session['id'])
    if request.method == "POST":
        quote = request.POST['quote']
        author = request.POST['author']
        posted_by = user
        thisquote = Quote.objects.create(quote = quote, author = author, posted_by = user)
        thisquote.save()
        return redirect(home)
    
def favorite(request, id):
    thisquote = Quote.objects.get(id = id)
    thisuser = User.objects.get(id = request.session['id'])
    print thisuser
    quotes = Quote.objects.all()

    if request.method == "POST":
        thisquote.fan.add(thisuser)
        thisquote.save()
        fav_quotes = Quote.objects.filter(fan = thisuser)
        context = {
            "thisuser" : thisuser,
            "quotes" : quotes,
            "fav_quotes" : fav_quotes 
        }
        
        return redirect("/home", context)

def user(request, id):
    users = User.objects.all()
    thisuser = User.objects.get(id = id)
    currentuser = User.objects.get(id = request.session['id'])
    their_quotes = Quote.objects.filter(posted_by = thisuser)
    count = Quote.objects.filter(posted_by = thisuser).count()
    context = {
        "thisuser" : thisuser,
        "their_quotes" : their_quotes,
        "count": count
    }
    return render(request,"pbelt/user.html", context )

def remove(request, id):
    thisquote = Quote.objects.get(id = id)
    thisuser = User.objects.get(id = request.session['id'])
    thisquote.fan.remove(thisuser)
    thisquote.save
    return redirect(home)

def logout(request):
    request.session["id"] = None
    request.session.clear()
    request.session.modified = True
    return redirect(index)