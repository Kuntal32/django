from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    context = {"title" : "Welcome Home"}
    return render(request , "home.html", context)

def contact(request):
    context = {"title" : "Contact Us!"}
    return render(request , "contact.html", context)

def about(request):
    context = {"title" : "About Us!"}
    return render(request , "about.html", context)

