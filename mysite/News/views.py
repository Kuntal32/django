from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import News, RegistrationData
from .forms import RegistrationForms

# Create your views here.

def home(request):
    context = {"title" : "Welcome Home",
               "mylist": ["Kuntal","Arup"]
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

def all_news(request):
    a_list = News.objects.all()
    context = {"title" : "News!",  "articals": a_list}
    return render(request , "all_news.html", context)

def register(request):
    context = {"title" : "Register","form":RegistrationForms}
    return render(request , "register.html", context)

def addUser(request):
    form = RegistrationForms(request.POST)

    if form.is_valid():
        register = RegistrationData(username = form.cleaned_data['username'],
                                    password = form.cleaned_data['password'],
                                    email = form.cleaned_data['email'],
                                    phone = form.cleaned_data['phone'])
        register.save()
        return redirect('add_user')