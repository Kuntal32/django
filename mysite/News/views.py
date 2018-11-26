from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import News

# Create your views here.

def home(request):
    context = {"title" : "Welcome Home",
               "mylist": ["Kuntal","soumaya"]
              }
    return render(request , "home.html", context)

def contact(request):
    context = {"title" : "Contact Us!"}
    return render(request , "contact.html", context)

def about(request):
    context = {"title" : "About Us!"}
    return render(request , "about.html", context)

def news_details(request):
    obj = News.objects.get(id = 1)
    context = {"title" : "News Details!","object":obj}
    return render(request , "news_details.html", context)

def year(request, year):
    a_list = News.objects.filter(pub_date__year = year)
    context = {"title" : "News Year!", "year":year, "articals": a_list}
    return render(request , "news_year.html", context)

