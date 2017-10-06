# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from models import * 

from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, "BREV/login.html")



def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect(index)

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name =  request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        user = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = password, confirm_password =  confirm_password)
        request.session['id'] = user.id


        
        # context = {
        #     "review" : review,
        #     "rating" : rating,
        #     "created_at" : created_at,
        # }
    return render(request, "BREV/home.html", {"user" : user})

def login(request):
    error = User.objects.login_validator(request.POST)
    if len(error):
        for e in error:
            messages.error(request, e)
        return redirect(index)
    else:
        email = request.POST['email']
        user = User.objects.get(email = email)
        request.session['id'] = user.id
        return render(request, "BREV/home.html", {"user" : user})

def new(request):
    return render(request, "BREV/new.html")


def home(request):
    user = User.objects.get(id = int(request.session['id']))
    print request.session['id']
    review = Review.objects.all()

    context = {
        "user" : user,
        "review" : review
    }
    return render(request, "BREV/home.html",  context)


def add(request):
    title = request.POST['title']
    author = request.POST['author']
    review = request.POST['review']
    rating = request.POST['rating']

    user = User.objects.get(email = email)

    book = Book.objects.create(title = title, author = author)

    rev = Review.objects.create(review = review, rating = rating, reviewer = user)

    return redirect('/home')

