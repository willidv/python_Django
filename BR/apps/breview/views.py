# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from models import * 

from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, "breview/login.html")



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
        alias = request.POST['alias']
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        user = User.objects.create(first_name = first_name, last_name = last_name, alias = alias, email = email, password = password, confirm_password =  confirm_password)
        user.save()
        request.session['id'] = user.id


        
        # context = {
        #     "review" : review,
        #     "rating" : rating,
        #     "created_at" : created_at,
        # }
    return render(request, "breview/home.html", {"user" : user})

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
        return redirect(home)

def new(request):
    return render(request, "breview/new.html")


def home(request):
    user = User.objects.get(id = int(request.session['id']))

    review = Review.objects.all().order_by("-id")[:3]

    reviews = Review.objects.filter(reviewer = user)
    
    context = {
        "user" : user,
        "review" : review,
        "reviews" : reviews
        
    }
    return render(request, "breview/home.html",  context)


def add(request):

    title = request.POST['title']
    author = request.POST['author']
    review = request.POST['review']
    rating = request.POST['rating']

    user = User.objects.get(id = request.session['id'])

    a = Author.objects.create(name = author)
    a.save()

    book = Book.objects.create(title = title, author = a)
    book.save()

    rev = Review.objects.create(review = review, rating = rating, reviewer = user, book = book)
    rev.save()
    
    print request.POST['review']


    return redirect(home)

def info(request, id):
    thisbook = Book.objects.get(id=id)
    review = Review.objects.filter(book = thisbook)
    context = {
        "thisbook" : thisbook,
        "review" : review
        
    }

    return render(request, "breview/info.html", context)

def user(request, alias):
    thisuser = User.objects.get(alias = alias)
    reviews = Review.objects.filter(reviewer = thisuser)
    count = Review.objects.filter(reviewer = thisuser).count()

    context = {
        "thisuser" : thisuser,
        "reviews" : reviews,
        "count" : count
    }
    return render(request, "breview/user.html", context)

def remove(request, id):
    review = Review.objects.filter(id = id)
    review.delete()
    return redirect(home)


def logout(request):
    return redirect(index)