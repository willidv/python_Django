# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from models import * 

from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "dashboard/login.html")

def new(request):
    return render(request, "dashboard/new.html")

def register(request):
    
    errors = User.objects.basic_validator(request.POST)
   
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect(new)
    
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if not User.objects.all():
            user = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = password, admin = True)
        else:
            user = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = password, admin = False)
        user.save()
        
        request.session['admin'] = user.admin
        request.session['id'] = user.id
        users = User.objects.all()
        context = {
            "users" : users,  
        }
        
        if user.admin ==True:
            return redirect(adminhome)

        else:
            return redirect(home)

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
            request.session['admin'] = user.admin
        else:
            return redirect (index)
            
        # print request.session['id']
        
        users = User.objects.all()
        context = {
            "users" : users  
        }
        if user.admin == True:
            return redirect(adminhome)
        else:
            return redirect(home)

def home(request):
    
    users = User.objects.all()
    context = {
            "users" : users,    
        }
    return render(request, "dashboard/home.html", context)

def adminhome(request):
    users = User.objects.all()
    context = {
            "users" : users,    
        }
    return render(request, "dashboard/admin_home.html", context)

def add(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect(new)
    
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = password, admin = False)
        user.save()
        request.session['id'] = user.id
        users = User.objects.all()
        context = {
            "users" : users
        }
    return redirect(home)



def message(request):
    if request.method == "POST":        
        person = User.objects.get(id = request.session['id'])
        receiver = User.objects.get(id = request.POST["userval"])
        message = request.POST['message']
        Message.objects.create(message = message, user = person, receiver = receiver)

        their_messages = Message.objects.exclude(user = person)
        context = {
            "thisuser" : person,
            "their_messages" : their_messages
        }

    return redirect( "user/"+request.POST["userval"])

def user(request, id):
    thisuser = User.objects.get(id = id)
    currentuser = User.objects.get(id = request.session['id'])
    messages = Message.objects.all()

    their_messages = Message.objects.filter(receiver= thisuser)
    their_followers = thisuser.followers.all()

    context = {                                       
        "thisuser" : thisuser,
        "their_messages" : their_messages,
        "their_followers" : their_followers
    }
    return render(request, "dashboard/main.html", context)

def user_edit(request, id):
    thisuser = User.objects.get(id=id)
    # print thisuser
    context = {
        "thisuser" : thisuser,
    }
    return render(request, "dashboard/user_edit.html", context)

def admin_edit(request, id):
    thisuser = User.objects.get(id=id)
    # print thisuser
    context = {
        "thisuser" : thisuser,
    }
    return render(request, "dashboard/admin_edit.html", context)

def update(request, id):

    thisuser = User.objects.get(id=id)
    
    if request.method == "POST":
        users = User.objects.all()
        thisuser.first_name = request.POST['first_name']
        thisuser.last_name = request.POST['last_name']
        thisuser.email = request.POST['email']
        thisuser.password = request.POST['password']
        thisuser.confirm_password = request.POST['confirm_password']
        thisuser.save()
        context = {
        "thisuser" : thisuser,
        "users": users
    }
        return render(request, "dashboard/main.html", context)


def remove(request, id):
    removee = User.objects.get(id = id)
    removee.delete()
    if request.session['admin'] == True:
        return redirect(adminhome)
    else:
        return redirect(home)

def follow(request, id):
    print "BOOMSHAKALAKA"
    thisuser = User.objects.get(id=id)
    currentuser = User.objects.get(id = request.session['id'])
    print "TRYING TO FOLLOW"
    print thisuser
    print "AS"
    print currentuser
    if request.method == "POST":
        currentuser.following.add(thisuser)
        currentuser.save()
    return redirect( user, request.POST["userval"])

def logout(request):
    request.session["id"] = None
    request.session.clear()
    request.session.modified = True
    return redirect(index)