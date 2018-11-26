
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home , name="home"),
    path('contact/', views.contact , name="contact"),
    path('about/', views.about , name="about"),
    path('news_details/', views.news_details , name="news"),
    path('year/<int:year>', views.year , name="year"),
]
