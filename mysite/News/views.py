from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    context = {}
    return render(request , "home.html", context)

def contact(request):
    context = {}
    return render(request , "contact.html", context)

def about(request):
    context = {}
    return render(request , "about.html", context)

